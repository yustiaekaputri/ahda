# AHDA dev6.1 — local test delivery

Download AHDA_Discovery_Engine_M1_Tasikmalaya_0.1.0-dev.6.1.zip from this directory.
Size: 119376 bytes.
SHA-256: 60a47eb5e6485b680ff152a04eb243a51bbcf7fe872e81098fe785d42d650f41

Development build for LocalWP only; do not upload to ahda.sch.id.
Preserve the existing Directory plugin and all database records. Back up LocalWP
before an operator-approved replacement of the Discovery plugin. Read the bundled
docs/M1_LOCALWP.md and M1_QA.md before installing or executing any commands.

The frozen 200-school Tasikmalaya scope is bundled. Offline tests pass on PHP8.2
and PHP8.4; actual WordPress/MySQL integration remains NOT TESTED. Network crawl,
publication and production remain disabled/unperformed. No secrets, wp-config.php,
full national data or database dump is included in this delivery commit.
