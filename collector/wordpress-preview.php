<?php
/** Read-only bridge preview. Execute only using wp eval-file, never as web endpoint. */
if (PHP_SAPI !== 'cli' || !defined('WP_CLI') || !WP_CLI || !class_exists('WP_CLI')) { exit(2); }
try {
    if (!current_user_can('manage_options') || strtolower((string) parse_url(home_url('/'), PHP_URL_HOST)) !== 'ahda.local'
        || !defined('AHDA_DIRECTORY_VERSION') || AHDA_DIRECTORY_VERSION !== '0.8.9') {
        throw new RuntimeException('LOCAL_ADMIN_DIRECTORY_089_REQUIRED');
    }
    $path = $args[0] ?? '';
    if (!is_string($path) || !is_file($path) || !is_readable($path) || filesize($path) > 131072 || strtolower(pathinfo($path, PATHINFO_EXTENSION)) !== 'json') {
        throw new RuntimeException('LOCAL_DRAFT_JSON_REQUIRED_MAX128K');
    }
    $raw = file_get_contents($path, false, null, 0, 131073);
    if (!is_string($raw) || strlen($raw) > 131072) { throw new RuntimeException('DRAFT_SIZE_LIMIT'); }
    $draft = json_decode($raw, true, 32, JSON_THROW_ON_ERROR);
    if (!is_array($draft) || !is_string($draft['npsn'] ?? null) || !preg_match('/^[A-Z0-9]{8}$/D', $draft['npsn'])
        || ($draft['status'] ?? '') !== 'pending_review' || ($draft['wordpress_apply_enabled'] ?? null) !== false
        || !is_string($draft['article_text'] ?? null) || strlen($draft['article_text']) > 10000
        || trim($draft['article_text']) === '' || preg_match('/[<>\x00-\x08\x0b\x0c\x0e-\x1f\x7f]/', $draft['article_text'])) {
        throw new RuntimeException('INVALID_PENDING_DRAFT');
    }
    global $wpdb;
    $wpdb->last_error = '';
    $schools = $wpdb->get_results($wpdb->prepare("SELECT id,npsn,name,visibility FROM {$wpdb->prefix}ahda_schools WHERE npsn=%s LIMIT 2", $draft['npsn']), ARRAY_A);
    if ($wpdb->last_error || !is_array($schools) || count($schools) !== 1 || $schools[0]['npsn'] !== $draft['npsn']) { throw new RuntimeException('EXACT_EXISTING_NPSN_REQUIRED'); }
    $school = $schools[0];
    $wpdb->last_error = '';
    $rows = $wpdb->get_results($wpdb->prepare("SELECT meta_key,LEFT(meta_value,16385) AS meta_value,OCTET_LENGTH(meta_value) AS value_bytes,verification_status FROM {$wpdb->prefix}ahda_school_meta WHERE school_id=%d AND meta_key=%s LIMIT 2", (int) $school['id'], 'profile_description'), ARRAY_A);
    if ($wpdb->last_error || !is_array($rows) || count($rows) > 1 || (isset($rows[0]) && ((int)$rows[0]['value_bytes'] > 16384 || $rows[0]['meta_key'] !== 'profile_description'))) { throw new RuntimeException('TARGET_METADATA_INVALID_OR_OVERSIZED'); }
    $old = $rows[0] ?? null;
    $old_has_value = $old !== null && trim($old['meta_value']) !== '';
    $identity_conflict = !isset($draft['identity']['name']) || $draft['identity']['name'] !== $school['name'];
    WP_CLI::line(json_encode([
        'mode'=>'READ_ONLY_COLLECTOR_WORDPRESS_PREVIEW', 'npsn'=>$draft['npsn'], 'school_id'=>(int)$school['id'],
        'existing_name'=>$school['name'], 'visibility'=>$school['visibility'], 'identity_name_difference'=>$identity_conflict,
        'target_key'=>'profile_description', 'old'=>$old, 'proposed_text'=>$draft['article_text'],
        'before_sha256'=>hash('sha256',json_encode([$school,$old],JSON_THROW_ON_ERROR)),
        'decision'=>$old_has_value?'PRESERVE_EXISTING_DESCRIPTION':($identity_conflict || $school['visibility']!=='publish'?'BLOCKED_IDENTITY_OR_VISIBILITY':'NEEDS_ADMIN_SOURCE_AND_CONTENT_REVIEW'),
        'source_identity_and_rights_verified'=>false, 'approval_recorded'=>false, 'apply_supported'=>false,
        'wordpress_posts_created'=>0, 'database_writes'=>0, 'network_requests'=>0,
    ], JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT|JSON_HEX_TAG|JSON_HEX_AMP|JSON_THROW_ON_ERROR));
} catch (Throwable $error) { WP_CLI::error($error->getMessage()); }
