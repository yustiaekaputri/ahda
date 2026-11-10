# AHDA development checkpoint

Date: 2026-11-09. Status: M1 PARTIAL — offline development increment complete;
real transport and LocalWP integration gates remain OPEN.

## Contracts and authorization

Read uploaded AHDA_AGENTS.md and AHDA_Codex_Master_Prompt_FastTrack.md in full;
copied them to repository root as AGENTS.md and master prompt. Continue actual
R4a, never rebuild the directory. User supplied both baseline ZIPs and approved
PHP tooling downloads. No live crawl, real DB write, production access, LocalWP
installation or publication has been executed. Production ahda.sch.id excluded.

## Source and changes

Original ZIPs preserved; extracted baseline under baseline/ with hashes in
qa/baseline-files.json. Directory unchanged. Development source is under
`development/ahda-discovery-engine`, version `0.1.0-dev.6.0`.

Added crawl policy, disabled pinned cURL adapter, frozen NPSN pilot validator,
read-only source-planning batches, separate m1_discovery_plan jobs with confirmed
local capability gate, leases/fencing, transaction checkpoint, resume, retry,
cancel, status and integrity-check. New ade pilot CLI registers only; no startup
network/cron/write. R2/R3/R4a code/schema remain unchanged except bootstrap/main
loads and version. New job type does not fetch, extract, verify or publish.

Changed/new file list and patch: docs/qa/development-diff.patch.
LocalWP guide and risks: development plugin docs/M1_LOCALWP.md and M1_QA.md.

## Tests

Logs: docs/qa/offline-tests.json and lint-php8.2.json / lint-php8.4.json.
PHP 8.2.32 and 8.4.24 run with -n. Six original Discovery suites pass (149 checks
per runtime), plus four new M1 suites; exact counts are in the logs. All ten
Directory standalone smoke suites pass under mocks. All PHP source files lint.
These are offline fixtures, not the user's schools, WordPress or MySQL proof.

## Known findings and unfinished work

- Actual Directory visibility is publish; some old fixtures use published.
- R1 legacy_hash is schema metadata only, not row data integrity.
- Old manual CLI lacks explicit capability checks in some paths; audit further.
- Native crawler remains hard-disabled and has no CLI fetch entrypoint.
  Need bounded DNS, durable per-host throttle across runs, real transport tests,
  and approved robots/terms/source policy before exposure. Generic proxy denied.
- Full manual parent-plugin security audit remains incomplete.
- Real LocalWP/MySQL integration: NOT TESTED. No real frozen pilot list supplied.
- M2 extraction/evidence/candidates, M3 admin review, M4 publication: NOT STARTED.
- Packaging is a development handoff only; production readiness NOT established.

## Next session

Do not repeat source inventory or passed offline suites unless code changes.
Read QA and handoff, review targeted diff and original hashes. Finish remaining
M1 transport/policy gates, extend CLI security review, and obtain the explicit
200-NPSN file. LocalWP is on user's machine, not cloud localhost. Before real DB,
network or install actions present exact impact and obtain scoped approval.
Never access wp-config.php/secrets, reimport, rebuild, or deploy production.
After an approved LocalWP planning test, record actual outputs and continue M2.
Rollback is restoring the original Discovery R4a ZIP on an approved backed-up
local installation; preserve M1 job rows and all legacy data, never drop tables.


## National NPSN input — follow-up 2026-11-09

User supplied nationwide text, not an explicitly frozen 200-school pilot.
Offline analysis/export DONE. 555,463 entries, 555,460 unique; duplicate codes
69931346, 70005045, 70005078 each occur twice. Unique partition: 530,732 eight-digit
numeric codes and 24,728 uppercase alphanumeric eight-character codes. Preserve
alphanumeric codes; existing numeric-only R3/M1 validation remains unchanged.
Matching counts alone do not establish matching database identities.

Outputs: data/npsn-national-2026-11-09/{master-unique.txt,
numeric8-pilot-compatible.txt,alphanumeric8-review.txt,report.json,README.md}.
New utility: tools/validate_npsn_master.py; tests/test_npsn_master.py.
Four Python unit tests PASS; national uniqueness/partition/hash checks PASS.
Evidence: docs/qa/npsn-master-tests.txt. No PHP plugin changes, so previous PHP
results stand without unrelated reruns. Existing development ZIP unchanged.
Original upload preserved; no network, real DB operations or pilot selection.
Next: explicit pilot selection and read-only matching against existing school
index (with school level and region); never treat numeric syntax as eligibility.
LocalWP database access is still unavailable in this cloud session.


## Regional pilot scope — follow-up 2026-11-09

User selected Jawa Barat and Jawa Tengah. Default documented allocation is 100
schools each, eligible forms SMA/SMK/MA/SMAK with visibility publish. Deterministic
ascending school_id within each province, intersecting the supplied national
master; never infer region from NPSN prefixes. No real schools selected yet.

Prepared data/pilot-jabar-jateng/scope.json, README.md and a read-only SQL export
template using the actual Directory schools schema and shipped regency map:
27 mapped Jabar regencies/cities (32), 35 Jateng (33). Query returns at most 1000
candidates per province, six school identity/classification columns only; actual
WP prefix must replace the placeholder. Query NOT EXECUTED; no DB connection.

Added tools/select_regional_pilot.py and tests/test_regional_pilot.py. Four unit
tests PASS: balanced stable selection, insufficient/master mismatch fails closed,
wrong region/level/visibility/formula/alpha rejection, duplicates and header checks.
QA log: docs/qa/regional-pilot-tests.txt. No PHP or ZIP changes.

Next external input: CSV from read-only LocalWP export containing school_id,
npsn,school_form,regency_raw,visibility,province_code. National NPSNs alone do not
contain these attributes. Do not invent or silently guess region/level. After
receipt run the selector, verify 100+100 and publish the frozen pilot file for
review; this does not authorize network/DB mutation/publication. Keep all existing
crawl and production gates. Rollback new tooling/docs/output only; no DB changes.


## Scope correction — latest user instruction 2026-11-09

SUPERSEDES the two-province 100+100 allocation and prior level restriction.
Select at most 200 STATE schools in JAWA BARAT ONLY. Prioritize SMP/MTs; only
if fewer than 200 exist, fill remaining slots with MA/SMA/SMK negeri in Jawa
Barat. Do not include Jateng, other provinces or private schools. Use explicit
ownership and province/regency evidence, never name/NPSN-prefix guesses. Stable
NPSN ordering per tier is a routine implementation default. If combined eligible
count is below 200, report shortage rather than relaxing constraints.

New uploaded ahda-nasional-2026.csv could NOT be transferred: download_file
returned "file exceeds the executor transfer limit of 32 MiB". Actual byte size,
CSV headers, contents and eligibility counts are UNKNOWN; no local CSV exists.
Tool discovery found no alternate upload/range-reading facility. No repeated
transfer attempts or invented results. Need ZIP <=32 MiB or smaller CSV parts
(with headers) / a Jabar-only export; keep original content and string NPSNs.

Saved current criteria in data/pilot-jabar-negeri/scope.json; prior regional scope
and README explicitly marked SUPERSEDED. No selection or output pilot yet.
No source/plugin/runtime/DB changes, network crawl or production action. No tests
run for this documentation-only scope correction. Existing M1 PHP eligibility
still excludes SMP/MTs: update + regression-test before feeding this new pilot to
M1. The old Python two-province selector must NOT be run for the new scope.


## Tasikmalaya workbook selection — 2026-11-09

Latest user supplied kab ko tasikmalaya.xlsx and instructed selection from it.
Input transferred successfully (464049 bytes), SHA-256:
fd02a73281cc85b9580b04a05c6e9f370421df8068cc3e615f4e1abfb81b4946.
One worksheet, 5763 data rows, 12 explicit classification columns. Only KAB.
TASIKMALAYA (4503) and KOTA TASIKMALAYA (1260); both map to Jabar code32.
Status explicitly NEGERI/SWASTA; no formulas or duplicate source NPSNs found.

235 eligible state candidates all match supplied national master: priority177
(SMP159/MTS18), fallback58 (MA10/SMA30/SMK18). Selected all priority177 plus
23 lowest-NPSN candidates from combined fallback: SMA21/SMK2, MA0. No quality
ranking implied. Final200: Kabupaten164, Kota36, all negeri, none outside Jabar.
Selection is now OFFLINE FROZEN; no random choice or live database validation.

Files: tools/select_tasikmalaya_pilot.py, tests/test_tasikmalaya_pilot.py;
outputs under data/pilot-jabar-negeri/tasikmalaya-200/ (TXT, CSV, JSON, XLSX,
report, README). scope.json updated. Six unit tests PASS plus actual source-row,
master membership, uniqueness, state/region/priority, hashes and generated XLSX
reopen/no-formula checks PASS. Log: docs/qa/tasikmalaya-selection-tests.txt.
Pilot TXT SHA-256: 42aaa7c51d5e0163c08146d1c46df70e260496639b9a3cc55e34f58781b1af20.

No PHP/ZIP changes or repeated unrelated PHP suites. No DB, network crawl,
publication or production operations. Important next work: M1 dev.6.0 currently
excludes SMP/MTS; update allowed forms under latest user scope, add regressions,
then validate frozen identities/ownership/region against read-only LocalWP data
before any approved write/run. Workbook validation is not proof of live DB or
independent official school verification. Rollback generated local files only;
original workbook and legacy records remain intact.


## Continued integration — dev.6.1 / 2026-11-09

User said "lanjutkan". Completed safe M1 integration for the selected 200:
- New pinned reference class and bundled 200-NPSN TXT/classification JSON.
- Scoped manifest JSON v2 binds NPSNs, current database IDs and reference SHA;
  database schema stays 1, no DDL and no parent/legacy record changes.
- Identity lookup_pilot adds ownership_status via SELECT; validates table prefix.
  Existing R3 lookup shape retained; original regressions unchanged.
- SMP/MTS support; scope requires frozen school form, NEGERI and exact Tasikmalaya
  regency. Checks at freeze and every batch, including resume after changes.
- Current CLI cannot enqueue unscoped jobs or run legacy unscoped jobs. Legacy
  reading/recovery/cancel and API compatibility remain; no data rewritten.
- CLI preflight defaults to bundled list, checks all200 with passed/failed/unrun
  and safe issue codes. Preview remains SELECT-only, defaults10, no fetch.
- All CLI mutations now reject --dry-run and require explicit matching confirm.

Canonical results in docs/qa/dev6.1: 12 suites on PHP8.2.32 and PHP8.4.24, 482
checks per runtime, all PASS; 39 development PHP files lint each PASS. Original
six R2/R3/R4a suite files byte-identical; all84 original baseline file hashes match.
New tests cover scope, reclassification/ownership/region, unknown/changed IDs,
SQL identifier/NPSN injection, preflight counts/errors, dry-run zero-query,
permissions, no legacy mixing, scoped enqueue/dedupe, failed scope checkpoint,
20 resumable fake batches and reference integrity. Actual NPSNs/classification
are fixture input only; database IDs and DB engine remain synthetic.
Independent temp-copy tamper test PASS; extracted ZIP offline runner PASS.

Artifact: artifacts/AHDA_Discovery_Engine_M1_Tasikmalaya_0.1.0-dev.6.1.zip.
Full changed-file list/diff/logs/checksums: docs/qa/dev6.1/. Previous dev.6.0 ZIP
preserved. New ZIP guides under plugin docs/M1_LOCALWP.md and M1_QA.md.
Frozen list unchanged, SHA 42aaa7c51d5e0163c08146d1c46df70e260496639b9a3cc55e34f58781b1af20.

Current-instance writes: code/local generated artifacts ONLY. No real DB,
network crawl, plugin installation/activation, production or publication.
Crawler remains hard-disabled; full DNS/transport/durable throttle gate OPEN.
LocalWP/MySQL8.4 integration NOT TESTED: user's ahda.local is not available in
this cloud executor. Full parent security audit and old manual CLI capability
hardening remain outstanding. M2 extraction/candidates, M3 review and M4 local
publisher still NOT IMPLEMENTED; do not call the MVP complete or production-ready.

Next action: user runs approved backed-up LocalWP installation and read-only
pilot preflight/preview according to handoff, then provides actual safe report.
Do not repeat passed offline audits without changes. Resolve classification or
identity mismatches without altering legacy data. Obtain scoped explicit approval
before any real job write, crawl or publish; no production scope. Continue M1
source permission/transport gates then M2 when prerequisites permit.
Rollback: restore original R4a ZIP locally after backup/approval; do not delete
M1 job rows or alter Directory. R4a ignores new job type. Dev.6.0 cannot process
new scoped v2 jobs; retain dev.6.1 for diagnosis rather than downgrading job data.


## GitHub artifact delivery — 2026-11-09

User explicitly approved uploading the prepared delivery branch and instructed
future package delivery via GitHub. Do not request the same upload authorization
again for routine future AHDA package delivery; preserve production/network/DB
approval gates. Avoid chat artifact links for this user.

Pushed ONLY ZIP + LocalWP delivery guide to GitHub yustiaekaputri/ahda,
branch delivery/tasikmalaya-dev6.1. Remote ref verified with git ls-remote:
62f2bd26cf42b2fd161b74bdfd7a31311f8868a3.
Files in uploaded commit:
- artifacts/AHDA_Discovery_Engine_M1_Tasikmalaya_0.1.0-dev.6.1.zip
- artifacts/LOCALWP-DELIVERY-dev6.1.md
ZIP SHA256 60a47eb5e6485b680ff152a04eb243a51bbcf7fe872e81098fe785d42d650f41.
No main-branch update/merge, production deployment or LocalWP operations.
The full workspace source/checkpoint remains local; this delivery commit contains
only the two listed files. The plugin source/tests/docs are included inside ZIP.


## LocalWP feedback + dev.6.2 source inventory — 2026-11-09

USER-REPORTED actual LocalWP output received, stored in
`docs/qa/localwp-dev6.1-user-report.json` (not cloud-executed).
- dev.6.1 schema postflight INSTALLED, complete,7 tables,0 missing, schema1.
- legacy METADATA SHA fbd684d9502cfe8cab5d91068f7c6829197837b3e2d29f67068f5c8076ada3b6.
- scope hash matches pinned reference; pilot200 checked/passed,0 failed/unrun.
- preview first10 successful, cursor27323, all10 Discovery links0/needs_source.
- DB-bound manifest hash c804d6044cbbf14f02178647a416c6f71118726517b3320b2dc96bcbe2d08dca.
This validates read-only scope/classification on user's installation, NOT actual
job writes, MySQL transactions, evidence record, native fetch, full200 sources or
absence of URLs from legacy metadata. Initial username placeholder failed;
operator then successfully used --user="admin". Use admin in future instructions.

Added dev.6.2 Source_Inventory and `wp ade pilot source-preview` command. SELECTs
only verified profile_website/profile_source_url metadata, official_website on
details, and four supported social platform URLs. Does not read contacts or pupil
data. Three bounded indexed reads per school, batch1–20; validates current frozen
scope via existing batch reader. Canonical dedupe retains origins; all new hints
remain pending/manual_only/fetch_permission NOT_GRANTED. Rejects unsafe formats,
platform mismatch, and sensitive query keys without echoing values. SQL/row
integrity errors fail closed rather than returning needs_source. No new writes.

13 suites PASS PHP8.2.32/8.4.24,512 checks per runtime;41 PHP files lint PASS.
New inventory suite30 checks, including CLI, dedupe, scope/permission, SQL failure,
query caps, sensitive tokens and cursor continuation. Full original regressions
and original84 baseline hashes unchanged. Logs/diff in docs/qa/dev6.2/.
One initial fixture error (invalid Facebook profile underscore) was corrected to
exercise valid-URL platform mismatch; final assertions unchanged/passing.

Packaged dev.6.2 for GitHub delivery per persistent user authorization; no main
merge, production, LocalWP install, real database write or live crawl by cloud.
Next external check: operator replaces ONLY Discovery on backed-up LocalWP, then
runs `wp --user="admin" ade pilot source-preview --batch-size=10 --dry-run` and
provides output. Avoid rerunning prior passed schema/pilot checks unnecessarily.
If hints exist, review source access/identity and obtain scoped approvals before
persistence or fetch. If no verified hints, source discovery still requires an
allowed source list/search adapter; do not enqueue empty planning work as a fix.
M2/extraction/candidates, M3/admin review and M4/publication remain unimplemented.
Crawl transport/DNS/durable-throttle gates remain open; no production readiness.
Rollback dev.6.2 to dev.6.1 after normal local backup/approval: no schema or data
migration, existing scoped v2 jobs remain compatible. Original R4a ZIP preserved.

GitHub dev.6.2 delivery completed and remote ref verified: delivery/tasikmalaya-dev6.2 at 271d7c06ec34ff6a21b6d0077c26ee6f02fb8cce. Prior ZIP and guide retained. No main merge/deployment.


## CLI naming defect + new LocalWP source evidence — 2026-11-09

User dev.6.2 reported source-preview NOT REGISTERED, suggestion source_preview.
Workaround immediately provided; user then successfully ran underscore spelling.
Root cause: WP-CLI does NOT convert reflected underscores into hyphens by default.
Prior stub/direct-method tests did not exercise native command-name resolution.
Corrected assumption; do not describe this as a data failure or failed install.

Actual USER-REPORTED source_preview output captured at
`docs/qa/localwp-dev6.2-user-report.json`: first10, cursor27323, scope/manifest hash
unchanged, links0, verified legacy URL hints0, rejected0, no requests or writes.
Do not extrapolate to all200 or infer schools have no websites. Further input
requires source acquisition, not creating empty planning jobs or repeated installs.

Hotfix dev.6.2.1 adds explicit WP_CLI registrations for four hyphen aliases while
retaining original underscore methods. Added8 bootstrap assertions; no SQL,
source reader, flags, schema or crawler changes. Existing6.2 works with underscore;
installing hotfix is optional for ongoing source discovery. Release to GitHub
under prior standing authorization after offline regression/package verification.

Prepared precise source-acquisition scope in docs/source-research-plan-first10.json:
10 existing first-batch schools, public education reference catalogs only,
20 HTTPS requests maximum,5s host interval,10s request timeout,256KiB cap,
one process, no automatic redirects, robots/terms respected, no social fetches,
DB writes, production or publication. Candidate hosts not yet independently
verified. Asked operator via async input for required network approval. Pending
approval is NOT authorization. No research network fetch has been made.


Operator approved catalog research via async reply "Izinkan pemeriksaan katalog
terbatas". Standing scope: first10 only, two named catalog hosts, total20 requests,
5s host interval,10s timeout,256KiB cap, no redirects/DB/production/social login.
Two robots requests attempted (one per host), both curl56 CONNECT tunnel403,
http000, zero body. This is cloud proxy failure before site response, not robots
or target content refusal. Current runtime observations enforced restricted
policy and neither catalog host allowed. No bypass/repeated attempts.
Budget used2,remaining18; successful catalog requests0; scope/ledger in
`docs/source-research-plan-first10.json` and `docs/research-first10/catalog-probes.json`.

Draft read tool failed INVALID_ARGUMENT (current draft could not be verified),
so unknown saved custom rules were not replaced. Runtime request_changes tool
unavailable. User needs to ADD referensi.data.kemendikdasmen.go.id and
referensi.data.kemdikbud.go.id to cloud environment network permissions. Do not
ask for the same research permission again. Retry only after policy change and
fresh enforced/current status, preserving remaining request budget and limits.

Unblocked hotfix:13 suites PASS on PHP8.2.32/8.4.24,520 checks each;41 PHP files
lint each. Bootstrap aliases explicitly tested, native LocalWP alias resolution
still NOT TESTED. SQL/parser/source reader unchanged; underscore source_preview
already works on user's LocalWP. Package dev.6.2.1 to GitHub per standing delivery
authorization; installation optional, no need repeat already-passed native tests.
No job/enrichment write, production action or successful catalog fetch occurred.

Hotfix dev.6.2.1 pushed to delivery/tasikmalaya-dev6.2.1, remote ref verified 57e95c674c750ab60dcdf9ee4d23fea6f0677c9b. Prior artifacts preserved. Research remains blocked by cloud allowlist; operator consent remains valid,18/20 requests left. No WordPress or production writes.


## Continued offline M2 foundation — dev.7.0 / 2026-11-09

User requested continue. Fresh runtime status: observations_current=true,
network policy enforced/restricted, neither approved catalog host allowed.
No repeated catalog requests (budget still2 used/18 remaining). Existing research
approval retained. Draft/runtime change tooling limitation unchanged; external
network settings block real source acquisition, not offline implementation.

Implemented ADE_Enrichment_Preview + `ade pilot extract`, structured JSON only:
- strict schema/types/byte/depth limits + duplicate/escaped-key rejection;
- immutable200-pilot scope, exact observed/source NPSN, explicit mismatch blocks;
- source content/quote/value literal containment; no fabricated fact generation;
- only profile_programs/profile_curriculum/profile_hours targets from actual
  Directory whitelist, protected keys/status injection blocked;
- plain UTF8/control/markup constraints, HTTPS URL/sensitive-key rejection,
  timestamp validation, stale evidence reason;
- deterministic evidence/candidate preview keys and dedupe; conflicting target
  values rejected; no facts/identity/permission certified by user document;
- current verified display snapshots from bounded prepared SELECT, school scope
  rechecked, snapshot hash and no-change marker; storage/publisher contract remains
  future work, this hash is NOT a publication authorization;
- previews always persisted=false, approved_value=null, not_ready/needs_evidence,
  no fetch/model/generation/write/publish. Demo fixture clearly synthetic and stale.

New files: includes/class-ade-enrichment-preview.php, data/examples/
m2-structured-fixture.json, tests/m2-evidence-preview-tests.php, docs/M2_PREVIEW.md.
Main/CLI/readme/QA updated, version0.1.0-dev.7.0. Existing R4a writers/identity-only
hint contracts unchanged. No browser endpoint/nonce-consuming mutation added.

14 suites PASS PHP8.2.32 and8.4.24,580 checks each;43 PHP files lint each. New M2
suite60 checks. All84 baseline files and6 original R2/R3/R4a tests unchanged.
Logs/diff/checksums in docs/qa/dev7.0/. LocalWP/MySQL M2 integration NOT TESTED;
real source permissions, HTML/CSV parsing, evidence/candidate persistence,
extraction worker, M3 review and M4 local publisher remain outstanding.

Deliver dev.7.0 ZIP + guide via GitHub standing authorization. New native smoke,
optional after normal backed-up/operator-approved LocalWP replacement:
`wp --user="admin" ade pilot extract --demo --dry-run`.
Expected FIXTURE_ONLY_READ_ONLY,3 in-memory candidates/evidence, false publication,
zero writes/requests, fixture/stale/identity/permission/review blockers. Synthetic
values must never be copied to actual profiles. Real data enrichment still0.
Do not require install just to fix cloud egress; dev6.2/6.2.1 source readers remain
usable. Keep known passed native scope/reader evidence without unrelated reruns.
Rollback to dev6.2.1 needs no migration/row removal; preserve all old data/jobs.
Next: resolve the two cloud catalog host permissions, use remaining18 budget and
operator-approved access only; then actual source evidence and native integration.

Dev.7.0 ZIP and guide pushed to delivery/m2-preview-dev7.0; remote ref verified b63c464fe047eeafd29dd6a988fd231744f117d0. Earlier artifacts preserved. Network source budget remains18; no catalog probes or real DB writes this continuation.


## Continued M2 pending persistence — dev.7.1 / 2026-11-09

User requested continue. Catalog policy freshly observed enforced/restricted,
no approved catalog hosts; no new probes.2 used/18 remaining still valid. Source
permission unchanged; no source/production network fetch or LocalWP writes.

Implemented ADE_Enrichment_Store with stage (read-only), store (explicit local
write gates, NOT EXECUTED on real DB), receipt (read-only historical diagnostics).
Guards: manage_jobs+review_candidates, operatorID, local WPCLI, schema preflight,
immutable200 scope, non-fixture and non-stale structured document, pre-existing
registered website/source-school relation, same host and known unblocked states.
No source auto-creation or source/identity promotion. Whitelist three meta targets
and literal evidence validation retained from7.0.

Store changes only Discovery candidates/evidence/candidate_evidence/jobs; no
legacy/profile/source/review writes. Source/current snapshots and expected row
states bind staging token. Stage exposes exact projected new rows/version bumps.
GET_LOCK0 per school; FOR UPDATE NOWAIT; atomic inserts + completed operation
receipt. Data errors roll back; repeat request reads receipt/no duplicates, even
simulated lost commit acknowledgment. Receipts bind result hash/provenance and
bounded payload sizes. No auto-approval/publish and all scores0. Existing reviewed
rows skipped unchanged, no evidence appended behind reviewer; pending additions
conditionally increment row_version. Source/snapshot/review/corruption races block.
Old evidence and proposals are never silently overwritten or deleted.

New files: includes/class-ade-enrichment-store.php, tests/m2-store-simulation.php,
docs/M2_STORE.md. Main/CLI/readme/docs and fake fixture helper updated. No schema
version or dependency/lockfile changes. Runtime remains dev, all automatic flagsOFF.

15 suites PASS PHP8.2.32/8.4.24,695 checks each;45 PHP files lint each. New store
suite115 fake checks, all10 insertion positions rollback, commit/ack loss,
idempotence, pending version race, changed review, approved-row immutability,
source/role/backup/confirmation, receipt/evidence corruption and CLI paths.
All84 baseline file hashes and6 original R2/R3/R4a tests unchanged. Canonical logs,
diff/checksums at docs/qa/dev7.1/. Real MySQL/LocalWP writer still NOT TESTED.

Asked async operator permission for isolated disposable MySQL8.4 tests in cloud,
synthetic data only, separate from LocalWP/production. No affirmative response yet;
DO NOT treat silence or code development approval as permission for real DB writes.
Plan: docs/NATIVE_MYSQL_TEST_PLAN.md. Runtime Docker skill read; explicit managed
unix socket check with endpoint/TLS/context selectors cleared succeeded (29.9.2),
user UID1000; official mysql8.4 image absent. No daemon/image/container/database
started, no secrets inspected/printed. Resource plan1CPU/1GiB and local-only port.
Need permission first, then install trusted test dependencies/pull official image,
run native SQL/lock tests under WP stubs, retain logs and remove own test container.
Label native MySQL under stubs separately from actual WordPress/LocalWP PASS.

Package7.1 + guide via standing GitHub authorization. Do not tell operator to run
store now: source/doc data not available/approved, native test gate open. Existing
demo extract remains read-only. No need install just for cloud network access.
M2 extraction worker, HTML/CSV parser, M3 review, post-commit revoke and M4 publisher
not complete. No real profiles enriched. Before LocalWP writes, review concrete
stage impact and obtain separate approval+verified backup. Native disposable
permission, if later granted, never authorizes LocalWP or production writes.
Rollback code to7.0 needs no migration; preserve any receipts/rows and use7.1 for
diagnosis. No post-commit delete/revoke implemented; full local publisher rollback
still future. Original R4a/Directory data and prior artifacts preserved.

Dev.7.1 package+guide pushed and remote ref verified at 507593aa5435c68cdd684ac3723cf7a61a626d5b (delivery/m2-pending-dev7.1). Prior artifacts preserved. Native disposable test consent still pending; no real DB/container created. Government source budget remains18; no new probes.


## 2026-11-10 — dev.7.1.1 WP-CLI dry-run hotfix

Operator reported invalid synopsis part --dry-run, unknown parameter for exact
extract --demo --dry-run. Our PHPDoc declared a mandatory boolean, which official
WP-CLI does not support. Earlier direct handler tests missed framework parsing.
Fixed extract/stage synopsis to [--dry-run]; handler requires boolean true, so
missing/negative flags still fail safely. Stage valued arguments documented.
No schema/writer/source/legacy/publisher changes or new runtime dependencies.

Added unmodified upstream WP-CLI v2.12.0 parser/validator/docparser/dispatcher
classes, pinned commit03d30d4138d12b4bffd8b507b82e56e129e0523f, MIT LICENSE and
per-file hashes in tests/vendor/wp-cli-2.12.0/UPSTREAM.json. Test-only; never loaded
by plugin runtime. New50 checks reproduce old error and invoke fixed handlers
through official factory/subcommand, scan all command synopses and check missing/
negative flag, CRLF and alias behavior. WP/config/help renderer/DB remain stubs;
this is NOT a complete WP-CLI binary or native WordPress/MySQL test.

16 suites,745 checks PASS each PHP8.2.32/8.4.24;55 PHP files lint each. All84
baseline hashes and6 original regression files unchanged. Logs/diff/error report
at docs/qa/dev7.1.1/. Native LocalWP hotfix retry NOT TESTED pending user output.
Previous preview error did not demonstrate any data change. Demo remains
FIXTURE_ONLY_READ_ONLY with3 synthetic candidates and0 writes/HTTP. No school
facts enriched. Native disposable MySQL consent still pending; no real DB or
container created. Catalog budget remains18, no new probes. Official tooling
source download does not consume the scoped school catalog request budget.

Delivery dev7.1.1 via previously authorized GitHub artifact branch. Install only
Discovery locally after backup, rerun exact demo command; no store/production.
Rollback plugin files needs no migration; preserve all data. M2 native writer
validation, source acquisition, extraction worker, M3 review and publisher gates
remain outstanding as above. No automatic publishing or production operation.

Dev.7.1.1 ZIP+guide pushed and remote ref verified at 91f2733430ae8ea655e9cf3af93e1133ab202b70 (delivery/m2-pending-dev7.1.1). Previous artifacts preserved; main and production untouched.


## 2026-11-10 — operator LocalWP demo retry PASS

User pasted successful exact command: wp --user="admin" ade pilot extract --demo
--dry-run. No invalid synopsis/unknown parameter error. Output mode
FIXTURE_ONLY_READ_ONLY, fixture_only true, school_id913/NPSN20268071,3 evidence
and3 candidates, all persisted false, approved_value null, not_ready. Reported
network_requests0/database_writes0/publication_enabled false. Expected fixture
blocks: unverified identity/permission, admin review, synthetic facts and stale
2020 evidence. These are intended gates, not a command failure. Sanitized output
and input hash: docs/qa/localwp-extract-demo-user-report.json. Installed version
not printed; do not claim independently verified version. This establishes only
operator-observed native demo preview success, not real extraction, native store
transactions, real school enrichment or publisher safety. No network/database
operations performed by cloud agent. No need rerun the same demo. Next: source
acquisition gate and native isolated MySQL validation (permission still pending);
continue safe offline milestones independently, never store fixture data.

## 2026-11-10 — dev.7.2 editorial draft + native MySQL validation

DONE (offline/native-under-stubs): new ADE_Article_Preview and pilot article
--demo|--evidence-file --dry-run. Builds escaped, evidence-linked HTML/string
preview, identity from existing unique NPSN index with frozen200scope validation,
three supported literal topics (programs/curriculum/hours), citations including
quotes/URL/fingerprint/time, metadata suggestions unapplied, twelve-topic editorial
checklist.9topics unassessed by adapter are explicit gaps, not assertions that
legacy data is empty. Every document claim unverified, approved count0; fixture
watermark embedded in HTML, original source/permission/stale/review blocks remain.
No profile_description candidate/write, no claims of full profile completeness.
One indexed school SELECT, no frontend hook/SEO duplication or auto work.

Changed runtime: new includes/class-ade-article-preview.php; main loads class and
version7.2; CLI shares bounded preview-file loader and adds article method. Writer,
Schema1/seven definitions, crawler, flags and legacy Directory unchanged. Added
article tests, updated official dispatcher tests, docs/M2_ARTICLE.md,
CONTENT_QUALITY.md, NATIVE_MYSQL.md and native opt-in harness. SHA-pinned upstream
WP-CLI files unchanged. SQLi/XSS/SSRF protection inherited document validation plus
HTML/attribute escaping, bidi/control/name bounds, strict identity, no Markdown
execution, explicit dry-run/capability/LocalWP guards. No new admin mutation/nonce
surface; article viewer/review UI is not implemented.

Operator answered explicit async "Izinkan uji MySQL sementara" this turn. This
supersedes pending disposable consent entries above; authorization covers only
isolated cloud synthetic test DB, NOT real LocalWP/production data. Read runtime
Docker/packages/network docs, confirmed managed socket29.9.2, pulled official
mysql8.4 with normal digest/TLS checks, installed signed Debian php8.2-mysql
locally. No global/runtime plugin dependencies. Password random ephemeral,
not printed or written to repository. Never read wp-config or user secrets.

Native tests PASS70checks on MySQL8.4.13, PHP8.2.32, actual Schema::create_sql and
InnoDB; wpdb adapter, WP/auth/local/preflight still stubs. Fixed database
ahda_m2_disposable, unique fresh container,1CPU/1GiB,512MiB tmpfs, loopback port,
no existing volume. Actual atomic writes/rollback all10positions, receipt replay,
actual committed state+simulated acknowledgment loss, evidence version advance,
two-session application lock and NOWAIT row lock, review change/stale plan,
reviewed row+links unchanged, current snapshot changed, quoted SQL literal and
legacy/source/review hash preservation tested. Article indexed read also tested.
Re-ran via packaged reusable opt-in Python harness to verify reproducibility;
70checks PASS again. Final harness cleanup hardening was retested (70PASS);
all three own containers/storage removed. Official image cache
retained. No other containers manipulated or daemon restart. Logs/digest/cleanup
at docs/qa/dev7.2/native-mysql-*. Output hash/raw schemas checked by native test.
Full WordPress/LocalWP writer/queue/publisher and real connection-failure behavior
remain NOT TESTED. Do not generalize native-under-stubs PASS to full WordPress.

17offline suites PASS on PHP8.2.32 and8.4.24:822checks each,58PHPfiles lint each.
New article suite72checks, official dispatcher55checks including exact article
flags. All84baseline hashes and6original R2/R3/R4a regression files unchanged.
Final logs/diff/baseline metadata at docs/qa/dev7.2/. No student personal data.

SEO source audit: baseline class-ahda-public.php already emits description,
canonical and School JSON-LD; sitemap/robots separate baseline modules. Preserved
all baseline hashes. No head hooks added, no fake last-updated/ratings/FAQ schema,
no automatic indexing/submission or ranking/AI recommendation promise. Existing
SEO/theme integration/rendering and VPS resource behavior remain untested.
Quality checklist includes admissions/fees/periods/facilities/accreditation/contact
and privacy rules.365day normalizer threshold not proof volatile facts valid.

IN_PROGRESS/BLOCKED: no real school documents sourced or profiles enriched.
Cloud environment refreshed: restricted/enforced, custom allowed_hosts empty;
reference domains still not permitted. No new catalog probes, remaining18of20.
Existing scoped operator research permission remains valid. Need environment
settings to add referensi.data.kemendikdasmen.go.id and
referensi.data.kemdikbud.go.id; saved draft persistence previously unconfirmed,
unknown saved allowlist must not be overwritten. No bypass or duplicate consent.
After policy actually applies, validate fresh allowed connection and bounded
robots/ToS-first research. Offline saved HTML/CSV adapter, multi-source conflicts,
extraction worker, M3admin review and M4publisher still outstanding. Extend only
actual Directory target allowlists, validate native and offline incrementally.

Delivery: package7.2 + guide via standing GitHub artifact permission, no main merge.
Operator can install Discovery locally after backup and run article demo only;
no store requested. Preserve Directory and all existing data. Rollback Discovery
files to7.1.1 requires no migration. LocalWP real writes need separate concrete
stage review/approval/backup; production excluded. Native harness is never invoked
by offline runner/plugin. Session checkpoint and evidence included in ZIP.

Dev.7.2 ZIP+guide pushed and remote ref verified at a2380cc16ff997741934d17fa28e39ae38f530b9 (delivery/m2-article-dev7.2). All earlier artifacts retained, main unchanged. Native test permission received and tests complete; no LocalWP/production writes authorized or performed.


## 2026-11-10 — operator LocalWP article demo PASS

Received successful wp --user="admin" ade pilot article --demo --dry-run output.
Mode EDITORIAL_DRAFT_READ_ONLY; fixture_only true; school_id913/NPSN20268071,
name read from existing index SMPN SATU ATAP 2 KARANGNUNGGAL, KAB.TASIKMALAYA.
3sections/3citations with valid internal links,9not_assessed_by_this_adapter gaps,
12topic checklist and approved0. HTML contains synthetic watermark. All sections
unverified/approved false; persisted false; network0/writes0/publication false.
Metadata not applied, canonical/schema not emitted. Expected source/review/fixture/
stale/full-profile blocking reasons retained; these do not mean CLI failed.
Sanitized output/hash: docs/qa/localwp-article-demo-user-report.json. Installed
version not printed; avoid claiming independent version verification.

Native operator-observed article demo command PASS only; no real school facts
extracted or profiles enriched, no public frontend/SEO/store/review test proven.
No need repeat demo or install another hotfix. Next: permitted source acquisition
(policy domain additions still needed) and offline parser/worker/M3 development.
Cloud disposable MySQL consent and completed70checks remain valid evidence as
previously scoped; not authorization for LocalWP/production writes. No network
or real database operation performed by cloud agent when recording this report.

## 2026-11-10 — dev.7.3 offline CSV/HTML adapters

DONE: ADE_Document_Parser plus pilot parse --format=csv|html --demo|--document-file
--dry-run. No HTTP/DNS/model/export/write/publish. Native read-only preview binds
frozen pilot identity/classification and existing verified meta snapshots. Output
raw_document_sha256, normalization version, structured_document and unverified M2
preview. Quotes refer to decoded/normalized records, NOT original raw HTML byte
slices. Raw original hash remains preview only; retain file/report together.
No source authority/permission verification or raw archive DB migration added.

CSV exact npsn,target_key,value header; UTF8/BOM,strict quoting/comma/CRLF/LF and
multiline support; no permissive broken-quote recovery, formula-leading cells,
extra columns, unsupported targets, mixed NPSNs, conflicting values.64KiB/20rows/
500byte values. Same old three target fields only; no arbitrary catalog schema
inference or teacher/student/private data collection. Structured CSV interchange
is not an adapter for every official dataset.

HTML actual PHP DOM,256KiB/10000nodes/depth32/20tables/64rows/20claims. Requires one
unambiguous non-nested two-column profile table containing expected NPSN. Exact
label map for programs/curriculum/hours only; ignored labels counted, not emitted.
Other visible named NPSN/duplicate identity/merged cells/multiple profiles block.
Inert HTML5 doctype allowed; XML/DTD/ENTITY/processing declarations rejected before
DOM parsing. NONET without NOENT/DTDLOAD, scripts/styles/noncontent/explicitly
hidden nodes removed, no assets fetched or script executed. External resource
resolver sentinel in tests observed0loads. CSS classes/stylesheets/JS/complex
layouts and DOM repairs still require human inspection; don't claim all hidden
text or every website layout is handled. Source content normalized explicitly.
Missing DOM returns M2_HTML_DOM_EXTENSION_REQUIRED before output, CSV unaffected.
Plugin boot/frontend does not invoke parser or add hooks. No schema/flags/writer/
Directory change. RequiresPHP7.4 header unchanged; tested PHP8.2/8.4 only.

Changed: new includes/class-ade-document-parser.php, CLIparse/main version7.3,
2synthetic fixtures, parser test, official dispatcher test, native test/harness,
optional local PHP_DOM_EXTENSION test runner support, readme/docs. No generated
SQL target expansion. Article7.2 and old extract unchanged. Source layouts/files
must be legally obtained by operator; source_url/time/reference are declarations,
not proof. Don't change fixture flag to turn demo into purported school facts.

18suites/945checks PASS each PHP8.2.32 and8.4.24 WITH actual DOM;60PHPfiles lint
both.18suites/892checks each WITHOUT DOM; HTML extraction explicitly NOT RUN there,
missing-extension guard verified (not counted as extraction PASS). Parser suite
116checks with DOM, official dispatcher62including both exact parse commands.
New suite tests formula/quote/identity/conflict/caps, XXE/external resolution,
hidden content, ambiguity, cell/depth/node/table/row/claim budgets, current scope,
capability/dry-run/local and no-write paths. Original84baseline hashes and6original
R2/R3/R4a suites unchanged. Standalone parser security suite observed0.038s and
19496KiBpeak RSS PHP8.2 cloud, not a VPS/frontend/batch performance guarantee.

Standing explicit operator disposable-MySQL consent reused, no repeated approval.
Read runtime Docker/packages/network references; daemon local29.9.2 confirmed.
Official signed Debian PHP8.2/8.4XML packages downloaded/extracted user-locally
under ahda-tools, no global/site installation. Default proxy/TLS/signatures kept.
No new catalog probes. Cached pinned official MySQL image reused,1CPU/1GiB,
512MiBtmpfs,random ephemeral password/loopback port, unique own containerIDs.
Native88checks PASS MySQL8.4.13/PHP8.2 with actual DOM/SQL/InnoDB and WP/wpdb/
preflight stubs, including CSV and HTML->stage->atomic pending writer->receipt
replay plus original70lock/rollback/review/snapshot/preservation checks. Final
native harness module-precondition hardening retested,88PASS. Both own disposable
containers/storage removed. Tests/scripts refuse missing opt-in; DOM/mysqli/
mysqlnd modules required before server creation. No other container touched,
secrets inspected, LocalWP/production operations or permissions inferred.
Final logs/digest/status/cleanup/diff at docs/qa/dev7.3/.

IN_PROGRESS/BLOCKED: no real school source fetched or profile enriched. Refreshed
runtime policy still enforced/restricted/custom allowed_hosts empty; two approved
reference domains not available, remaining research18/20 unchanged. No bypass or
duplicate operator research consent. Need saved domain additions/applied policy,
then bounded robots/ToS checks. No confirmed draft persistence. Sources must be
real/authorized before actual candidates can be useful. Parser breadth, raw
archive binding, resumable M2worker, M3review/dashboard and M4publisher/rollback
still outstanding. Native/full WordPress/LocalWP parser and frontend SEO tests
NOT TESTED. Canonical/School schema/Directory source unchanged; no ranking/AI
recommendation claims. See M2_DOCUMENT_PARSER.md and latest quality/security docs.

Delivery7.3 via standing GitHub permission, ZIP/guide on new artifact branch only.
Local demo tests optional after Discovery-only replacement+backup; don't rerun
older successful article demo, reimport, rebuild or install schema. No store or
production request. Rollback files to7.2 without migration; preserve all tables.
Next safe work: source-specific validation/archives and extraction worker or M3
review using synthetic tests, preserving source/review/publisher separation.

Dev.7.3 ZIP+guide pushed and remote ref verified at 5c7264b667f4ee52a574736ad1fb6c21be848425 (delivery/m2-parsers-dev7.3). Earlier artifacts preserved; main/production unchanged. Both own disposable test containers removed; LocalWP parser retry remains NOT TESTED pending operator output.


## 2026-11-10 — operator LocalWP CSV and HTML demos PASS

User output confirms both pilot parse --format=csv|html --demo --dry-run succeed,
3candidates each, fixture true, school_id913, zero network/writes and publication
false. No warning/error. Installed version not printed; not independently proved.
Sanitized evidence at docs/qa/localwp-parser-demo-user-report.json. No need repeat
old demos/install another parser hotfix. Not real sources/enrichment/native writer
or frontend/SEO PASS. Continue M3 read-only candidate inspector safely, keeping
review decisions/publisher separate and disabled.

## 2026-11-10 — dev.7.4 M3 read-only candidate inspector

DONE (M3 read-only foundation, NOT decision workflow): WP Admin AHDA Discovery >
Kandidat (baca-saja). Server local site/current actor/ade_review_candidates guard
on controller AND service, dependency/schema/safe-flags preflight, frozen pilot
identity/classification recheck. No operational feature flags enabled, migrations,
new options/roles, POST/action/AJAX/REST/nonce mutation endpoints or writes added.
No source requests, cron, full-directory COUNT/OFFSET scans or frontend SEO hooks.
Empty chooser reads bundled200reference only; no candidate/schema query until
school selected. One indexed school lookup, M2types only, existing target3allowlist.

Candidate list20+1 keyset, optional status filter. Details bind candidateID AND
schoolID/type; comparison current VERIFIED meta vs original snapshot/proposal/
stored approved value. Current hash uses exact M2namespace; conflict warning only,
never overwrite. Evidence20+1 keyset with same-school/target/value/type/parse/scope
checks. Corrupt cross-school links block, raw observed JSON/private notes omitted.
HTTPS URL validated/redacted if credential/IP/token-query; no DNS or fetch. Quotes,
time and source relationship/status shown escaped. Warnings for missing/pending/
stale/invalid source conditions, permission always independently unverified.
Readiness reasons capped/page-scoped, not full source certification. View multi-
query reads not atomic; any future mutation must revalidate transactionally.
No approve/edit/reject/defer/audit append/publish controls or handlers exist.
No ranking/confidence/complete-profile claims. CLI demos don't populate this UI;
empty list expected, never store synthetic facts just to fill dashboard.

Runtime changes: new includes/class-ade-candidate-inspector.php and
admin/class-ade-admin-review.php; main version7.4 loads service; existing bootstrap
loads view only in admin, existing menu adds submenu. Registration has no query/
network/write side effects. Old CLI/schema/queue/store/parser/Directory preserved.
Test changes: new m3-inspector-tests.php, toggleable ready flag in fake preflight
helper, extended native SQL tests, opt-in standalone browser fixture/generator/
Playwright tests. Source/SQL targets still only Discovery reads + exact verified
legacy meta read. No production access, credentials or wp-config read.

19offline suites PASS each PHP8.2.32/8.4.24 WITH DOM:1010checks each,65PHPfiles
lint each. Without DOM957checks each; HTML extraction explicitly not run there.
Inspector suite65checks covers caps/local/preflight/scope/IDOR/pagination,
current-value conflicts, overflow/duplicate current, corrupt evidence, URL/token
redaction, XSS across name/proposal/snapshot/quote, unsafe GET and SQL error hiding.
84baseline file hashes and6original R2/R3/R4a suites unchanged. Final QA at
/docs/qa/dev7.4. An initial QA log output directory reused7.3; current logs moved
to7.4 and original7.3 logs restored byte-for-byte from delivered ZIP before release.
No historical artifact changed or rewritten.

Native110checks PASS MySQL8.4.13/PHP8.2 actual SQL/schema/InnoDB under WP/wpdb/
preflight stubs, previous88 plus inspector list/status/cursor/detail/hash/current
conflict/IDOR/cross-school evidence/token URL masking and all9synthetic table row
hash preservation. Reused existing explicit disposable consent, pinned cached
image and managed socket29.9.2;1CPU/1GiB/512MiBtmpfs, random password/loopback port,
own unique containerID. Test container/storage removed, no other container or
LocalWP/production touched. Native WordPress preflight/role/menu execution still
NOT TESTED. No stronger integration claim than SQL under stubs.

Browser16checks PASS actual PHP view in headless system Chromium via existing
Playwright, synthetic WordPress/backend/data stubs + minimal CSS. GET school
selection/list/detail, citations, conflicts, empty state, script nonexecution,
no POST forms, unauthorized/site403, desktop1280/mobile390 and no page overflow/
external requests. Screenshots in qa/dev7.4, manually inspected desktop. All
nonloopback browser requests aborted by harness; zero attempts observed. Initial
bundled Playwright browser path missing, resolved to existing /usr/bin/chromium
without downloading. Initial fixture403 response buffering fixed in test harness,
not product capability guard; final16PASS. Fixture requires cli-server+explicit
synthetic env flag, normal web/PHP-FPM requests404; generator CLI+optin only.
Standalone test server stopped. Not real WordPress/LocalWP admin/theme rendering.

IN_PROGRESS/BLOCKED: no real source or school profile enriched; source domain
policy unchanged/enforced/custom allowlist empty, remaining catalog research18/20.
No new probes or configuration claims. Existing scoped research permission stays
valid; policy additions needed before robots/ToS-first requests. M3decision/audit/
identity-permission verification, raw document archive binding, M2resumable worker,
broader fields and M4publisher/rollback remain outstanding. Must not approve on
literal quote or snapshot alone. Sources/documents untrusted; no private student
data. Full native LocalWP inspector and VPS/frontend SEO/WordPress plugin-theme
integration not tested. Previous user CSV/HTML demo PASS scoped to those commands.

Delivery7.4 ZIP+guide via existing GitHub artifact authorization, no main merge or
production deployment. Local operator may replace Discovery after backup then
open new read-only menu; no need repeat successful CLI demos or modify DB. Missing
menu/cap/blocked preflight should be reported, not silently remedied with role/
option writes. Rollback Discovery files to7.3 without migration; preserve all data.
Checkpoint/evidence/screenshots included for next session to continue safe M3
workflow/source contracts and tests without re-auditing the completed foundations.

Dev.7.4 ZIP+guide pushed and remote ref verified at 36693bd7f9dc6de427210304e846118605d3d934 (delivery/m3-inspector-dev7.4). Previous artifacts/main preserved. Own native container and browser fixture server stopped; no LocalWP/production write performed. User LocalWP inspector render remains pending.

## 2026-11-10 — dev.7.5 negative review foundation (default OFF)

DONE/tested under isolated stubs: reject/defer service, actor/action/version-bound
plan, WP nonce verification API, POST controller, strict request schema/reasons/
plain500byte note, scoped pilot/capability/current actor/local/preflight/backup+
per-action confirmation. Negative transitions only new/deferred->deferred/rejected;
rejected terminal, approve/edit/publish/reopen always unavailable. No permission/
source verification or profile/evidence/proposal/base hash/approved field mutation.

Standard package leaves ADE_LOCAL_NEGATIVE_REVIEW_ENABLED undefined/OFF; no new
write handler registered, no forms unless separately opted in. No options/caps/
wp-config changes. Existing automatic flags stay OFF. Inspector default remains
read-only and adds paginated negative audit history. Do not enable real writes
now; future LocalWP gate requires concrete candidate impact, real nonce/role/
preflight integration, backup and separate operator approval. Never production.

Plan digest binds current candidate values/version/base/snapshot SHA and actor,
action, frozen scope. Same application lock as M2 per-school, GET_LOCK0 plus
FOR UPDATE NOWAIT; transaction rechecks candidate/scope and CAS version/status/
approval-null fence. Changes exactly one candidate status/version/updated_at,
appends one reviews row and one completed jobs receipt. No audit UPDATE/DELETE.
Audit holds reason/actor/time/before/after/version/note; nonce not persisted.
Receipt operation namespace unique, request hash and result hash; replay validates
referenced audit fields/operation/notes too. Exact retry returns historical result
without duplicate audit, including after a later negative decision. Failed status/
audit/receipt/commit rolls back. Actual COMMIT followed by simulated acknowledgment
loss resolves via receipt; controller warns unknown results require status/history
check. No post-commit undo/reopen implemented; do not delete/rewrite audits.

Controller POST only, typed IDs, wp_unslash once, feature+cap+site+nonce+confirm in
service, fixed wp_safe_redirect to re-read state (no GET success flag trust),405GET/
403invalid/409stale or busy/503internal uncertain outcome. Conditional forms have
separate scoped nonce/reason/note/backup+impact confirmations, no approve/publish.
Labels/banner/menu accurately distinguish enabled synthetic-test negative mode
from default readonly. Audit notes escaped; no raw JSON/private source notes sent
to frontend or public profiles. Source URL rendering unchanged. History20+1 keyset.
Tunda does NOT automatically resume M2: reviewed candidates frozen against hidden
evidence additions. Explicit audited reopening is future work, not manual SQL.

Runtime: new includes/class-ade-review-decisions.php, main7.5 include; inspector
reports negative enable state + approvalfalse, admin review conditionally registers
handler/forms/history, bootstrap invokes no-op register when OFF. Existing store,
parser, schema1/seven definitions/Directory untouched. Test helper actor toggles
only in stubs; new m3-decisions-tests and CLI child handler fixture, native SQL and
browser opt-in fixture extended. Default bootstrap regression proves no additional
write hook, source/cron/network/schema activity. All84baseline hashes and6original
R2/R3/R4a suite files unchanged.

20offline suites PASS each PHP8.2.32/8.4.24 WITH DOM:1121checks each;68PHPfiles lint
each. Without DOM1068checks, HTML extraction explicitly not run there. Negative
suite111checks includes disabled/roles/nonce actor+action/version/plan actor,
types/reasons/plaintext/scope/IDOR/stale content/version, locked approvals/states,
rollback audit/receipt/CAS/commit, unknown outcome, receipt/audit corruption and
separate controller child requests typedIDs/unslash/redirect/GET405/invalid403/
stale409/approve refusal. Fake nonce provider is NOT real WordPress HMAC/session.

Native146checks PASS MySQL8.4.13/PHP8.2, actual schema/SQL/InnoDB, under WP/wpdb/
preflight/nonce stubs. New decisions/status/audit/receipt/replay/history/terminal
reject/forbiddenapprove, audit and receipt insert rollback, stale external version,
M2/M3 shared GET_LOCK, NOWAIT two-session conflict, actual commit+simulated ack
loss, unchanged legacy/source/evidence and M2 leaving reviewed rows/links alone.
Two own disposable containers used (initial141 then final146 expanded coverage),
both storage/containers removed; cached pinned image retained. Standing explicit
synthetic MySQL consent reused;1CPU/1GiB/512MiBtmpfs, own generated secrets/port,
managed socket29.9.2. No real LocalWP DB, production, wp-config or secrets read.
No altered daemon/other containers. Logs/digest/cleanup at docs/qa/dev7.5.

Chromium21checks PASS actual PHP template, synthetic WP/service/data stubs/minimal
CSS, desktop/mobile/default and opt-in negative forms with nonce and required two
confirmations. No POST actually sent by browser; controller positive/negative
covered separately under fake WP/DB. XSS nonexecution also for historical note;
no external requests. Screenshots synthetic and manually inspected. Browser fixture
case flag only exists in guarded cli-server test file; cannot enable real plugin
with GET. Own fixture server stopped. Full native WordPress admin routing/cookie/
nonce/session expiry/capability/preflight and LocalWP writes still NOT TESTED.

IN_PROGRESS/BLOCKED: full M3approval/source permission/identity verification,
compensating reopen, raw source archive binding, resumable M2worker and broader
content fields, M4publisher/rollback all outstanding. No school facts/profile
enriched, no public SEO changes. Runtime refreshed restricted/enforced/custom0;
reference catalogs still unallowed; no new probes, research budget18/20 remains.
Existing scoped operator research permission not re-requested. No confirmed draft
policy change and no bypass. Need source availability/permission before real
content, full WordPress write validation before local operator write trial.

Delivery7.5 ZIP+guide via standing GitHub authorization; no main merge/deployment.
No new CLI demo needed, no requirement to reinstall immediately. If installed,
default remains read-only, empty history normal. Do not enable constant/roles/
options or modify wp-config for a real write now. Rollback files to7.4 without
migration; preserve audits/receipts/data. Checkpoint/QA docs for next session.

Dev.7.5 ZIP+guide pushed and remote ref verified at eafc1a2f0d4bba8706cd2c39aa9aad6de3943044 (delivery/m3-negative-dev7.5). Prior artifacts/main preserved. Both own disposable native containers and browser fixture server stopped. Default review writes OFF; no user LocalWP/production operations performed.

## 2026-11-10 — dev.7.6 real WordPress integration validation

DONE: reproducible real WordPress7.1.4 + Directory0.8.9 + Discovery7.6 synthetic
admin integration. Actual WP login/cookies/roles/capabilities, wp_verify_nonce from
wp-includes/pluggable.php, actual wpdb and admin-post controller routing. No stubs
for those subjects. Official WordPress dependency tag7.1.4 pinned Git SHA
 db96f5eaa77a8d3e8eec8923a518fa2326f0d46a, obtained via allowed HTTPS Git tooling,
cache /workspace/ahda-tools/wordpress-7.1.4 unchanged. Core dependency not bundled.
Signed Debian PHP8.2-common previously downloaded extracted locally for ctype/
iconv/fileinfo; DOM/mysqlnd/mysqli already local. No global or user-site install.

New tests/wordpress/bootstrap.php, control.php, run-isolated.py, e2e.spec.cjs and
README, docs/WORDPRESS_INTEGRATION.md. No user wp-config read/write/generated.
Only owned TEMP core wp-load.php copy shim calls environment bootstrap + real
wp-settings. Original Core cache unchanged, post-run no-config assertion PASS.
Standard actual plugins copied/activated; Directory creates fresh EMPTY legacy
schema in NEW isolated DB, actual R1 installer creates7Discovery tables.2synthetic
schools +3M2-shaped pending candidates/evidence seeded via actual wpdb, not the
M2CLI/store API (do not claim that end-to-end path). No555460profile import/rebuild,
no actual user data/DB/config/production. Mail and ALL background HTTP blocked via
real early WP filters, cron/updaters/file modifications/search indexing disabled.

Test admin siteurl owned127.0.0.1 port, home alias ahda.local only for unchanged
local-host guard. No connection to real user ahda.local: browser route aborts
non-owned origins, all API POSTs fixed loopback/maxRedirects0. Test-only rest_url
maps Core self REST URLs to owned loopback; allowed_redirect_hosts permits127
for this split-URL setup. Not a production configuration recommendation. WP
functions remain real. Actual user Windows/LocalWP config remains untested.

Five owned disposable DB/site/server runs: first2 failed strict external-attempt
assert (Core REST chose home alias), all attempted alias requests ABORTED before
connection. Harness REST origin corrected, no plugin behavior workaround. Third
33checksPASS, fourth39expandedchecksPASS, final39PASS with provenance/cache/
no-config assertions. Earlier FAIL evidence retained with cleanup states in
qa/dev7.6/attempt01 and attempt02, earlier successes separately. No failures
relabeled. Each owned DB/container/temp site/server fully removed in finally.
Cached official MySQL digest reused,1CPU/1GiB/512MiBtmpfs, ephemeral loopback
ports/secrets. Standing explicit cloud synthetic MySQL consent reused; no fresh
operator permission inferred for LocalWP/production. No other daemon/container
modified/restarted. WordPressmail suppressed before install; no messages sent.

Final39real WP checks PASS: real preflight/role grants/admin authentication,
anonymous redirects/POST400, editor view+write403, default no handler/forms,
controlled test-only switch ON/OFF, nonce generation/invalid/action/login-session
binding, backup acknowledgment, unconditional approve refusal, untrusted redirect
ignored/safe target, actual status/audit/receipt/quoted SQL-looking backslash note
roundtrip, HTTP replay idempotence, audit rendering, defer->reject/terminal,
stale version409/no audit, cross-school IDOR, stored quote/proposal XSS escaping
actualWP, desktop/mobile no page overflow, approved/publication NULL/not_ready,
source/evidence/link and ALL25synthetic AHDA legacy table row hashes unchanged.
No external attempts on final run. Nonceprovider/adapter provenance recorded,
actual WordPressadmin screenshots manually inspected. Synthetic warning prominent;
opt-in screenshot does NOT mean feature enabled in user site. Raw passwords,
auth seed/cookies/nonce form bodies not saved to reports. Safe own logs only.

20offline suites1121checks each PHP8.2.32/8.4.24 WITH DOM;1068without DOM (HTML
not run there),70PHPfiles lint each, all84baseline hashes/6original regression
files unchanged. Runtime PHP compared byte-for-byte against7.5 ZIP: main header/
version7.6 only, all other root/includes/admin files identical. Review defaults
OFF, same behavior; no new fields/approval/publisher/network/automatic jobs.
Previous146native-SQL-under-stubs/21fixture-browser evidence retained as prior
version scope; not rerun/recast as new checks. Final proof in docs/qa/dev7.6.

LIMITS: isolated real WP with custom bootstrap/home/REST alias != user LocalWP
end-to-end, third-party plugins/public theme/frontend SEO/VPS load untested.
WPnonce expiry clock stress, real TCP commit failure/deadlock/load not exercised.
M2fullCLI/storeWP bootstrap not tested; fixtures intentionally use wpdb setup.
Positive approval/source permission/identity attestation, raw archive binding,
resumable worker/broader fields, compensating reopen and M4publisher/rollback
remain outstanding. Real source/catalog access still restricted/enforced/custom0;
no new probes, remaining research18/20, standing scoped permission preserved.
No factual profiles enriched or ranking/AI recommendation promise.

Deliver7.6 source/harness/QA ZIP+guide via existing GitHub permission, no main merge.
No immediate reinstall/repeated demo required: this update supplies test evidence,
keeps actual site write feature OFF. Before any real LocalWP change need concrete
candidate plan+backup+separate operator approval. Preserve all old data/audits;
rollback files to7.5 needs no migration. Next safe development: source/archive
contract and worker or audited reopen, then approval/publisher only with evidence.

Dev.7.6 ZIP+guide pushed and remote ref verified at 01da54c7b4acb6fa62a6466086db1039f8e09bf6 (delivery/wp-validation-dev7.6). Earlier artifacts/main preserved. All5own isolated WordPress DB/site/server runs cleaned. Actual user LocalWP/production untouched; writes remainOFF.

## 2026-11-10 — dev.7.7 local archive/checkpoint preview worker

DONE (offline foundation): classes strict-json/local-archive/local-worker and
shared normalizer integration (three new classes, existing normalizer refactored),
CLI `pilot archive` synthetic output and `pilot work` strict dry-run, version7.7.
Archive exact frozen200 / max4MiB, <=200inline documents, <=3/school, CSV/JSON64KiB,
HTML256KiB; validated raw+metadata hash and deterministic canonical manifest.
UTF8/HTTPS/URLsecret/size/key/scope limits; shared duplicate-key JSON scanner has
allocation structural-token budget50000/depth16 before decode. No HTTP/DB/file
write path, no new role/options/tables/migration/frontend/cron. Only existing
identity prepared SELECT through localCLI capability/preflight guard.

Worker computes<=10/call, soft5s deadline between schools, prefix checkpoint bound
to manifest/pipeline/scope, preserves previous summaries, resumes without replaying
prefix. Retry failed/conflict/identity only <=3attempts, others/cursor unchanged.
Same field conflicts across docs block entire school's candidate output; malformed
one document also blocks whole school without aborting following schools. Matching
claims retain separate raw-document evidence refs; unapproved/not_ready always.
CLI actual live identity/classification recheck for newly processed schools;
pure test invocation without resolver explicitly marks LIVE_IDENTITY_NOT_CHECKED.
Checkpoint checksum operator-controlled, NOT cryptographic origin/permission,
commit receipt, approval or durability guarantee. No durable database worker,
transactional checkpoint, lease/fencing, raw filesystem archive or store bridge.

PASS:21offline suites1230checks per PHP8.2.32/8.4.24 WITH DOM;1166withoutDOM (HTML
not run).74PHPfiles lint each.84baseline hashes and6original regression files
unchanged. Worker suite95checks DOM/84without, plus officialWPCLI2.12 dispatcher
76checks including actual file/checkpoint read, strict flags/local/capability gate.
Failures during development: first JSON metadata negative fixture still contained
old sourceNPSN, corrected entire fixture identity; local-gate expected error fixed
to existing LOCAL_OPERATOR_GATE_BLOCKED. Final suites clean, no warnings/errors.
New tests cover escaped duplicate JSON/4MiB input/token allocation limit, archive
hash/scope/size/URL/reference, conflict/identity, resume200, checkpoint corruption,
manifest drift, retry limits, deadline/no skipped cursor, provenance and JSON binding.

Measured cloud synthetic only:3,322,738byte/200document archive, batch10HTML each
~200KB, PHP8.2 memory_limit128M:0.423s, peakPHP13,971,456bytes. Not actualWordPress
RSS/VPS load certification. No source facts, external requests or realdatabase
operations in new worker tests. NativeWordPress39checks remain dev7.6 prior scope,
NOT rerun/relabelled; worker7.7 userLocalWP/nativeWordPress integration NOT TESTED.
Evidence docs/qa/dev7.7, contract/Windows commands docs/LOCAL_ARCHIVE_WORKER.md.

Known limits: report retains only current batch full results; preserve each report,
checkpoint retains summaries/hashes only. Input checkpoint/report512KiB max; use
checkpoint property alone for large reports. Soft deadline excludes archive decode
and cannot interrupt one school. `complete` means200checked, not200enriched. Demo
1preview/1conflict/1badNPSN/197needs_source with DOM, stale/synthetic blockers remain.
A rehashed operator checkpoint may skip previews but cannot authorize any mutation.
Report redirection is explicit shell write outside webroot, never overwrite input.
No positive approval, factual source attestation, native raw-archive evidence store,
transactional durable extraction worker or publisher/postcommit undo implemented.

Safe rollback pluginfiles to7.6, no migration; retain olddata/audits/operatorfiles.
Production/userLocalWP untouched. Review writes/network/publication defaultOFF.
Standing catalog research permission still18/20requests/first10schools; network
status refreshed restricted/enforced/custom0, govt hosts unavailable, no new probes
or bypass. Next: source archive provenance-to-pending storage contract, review
permission/identity gate, then durable lease/fenced worker before localpublisher.
Deliver7.7 ZIP+guide on newGitHubdeliverybranch under prior permission, preserve main.

Dev.7.7 ZIP+guide pushed; remote ref verified 6ba399ca10fcc08202edc09477cedd9f2ba4f010 (delivery/local-worker-dev7.7). Only2new artifacts; main/earlier packages preserved. No actual school facts enriched. Source/ZIP immutable release contents verified before delivery.

## 2026-11-10 — dev.7.8 archive review bridge and multisource draft

DONE read-only: new ADE_Archive_Review and `wp ade pilot inspect` strict dry-run
for one member of existing200. Raw archive always reparsed by new worker inspect
method, no checkpoint/report authority. Actual identity/classification lookup,
current verified meta snapshot<=3fields/16KiB + base hash/change comparison,
explicit <=3document-to-registeredURL bindings with same-host HTTPS/secret hygiene,
prepared JOIN school/sourcecanonicalkey LIMIT2. Missing/blocked/ambiguous/unknown
source relations held; no source auto-create, official promotion or attestation.
Plan checksum covers actor/raw/manifest/current/source states, NOT approval/store
capability. All storage/approval/publication flags false; no new mutation code.
Old manual structured store remains separate, unchanged; no archive store added.

Multisource article reuses private renderer after independent raw validation:
matching claims combine multiple citations, each raw_document_sha256/documentkey/
format retained.3supported fields only;9other topics explicitly unassessed, never
filled by inference. Conflict/badNPSN/no-doc -> no article. Name/value/URL escaped,
synthetic/unverified warning, title/description proposals never applied; no public
SEO/schema hook. Existing structured single-doc fixture output byte-identical to
7.7 on frozen clock (SHA9096c88b17e645318475d85749dc8b7cb952ec08a2c556a1fbb08e2a64c9a48a).

PASS22offline suites1371checks each PHP8.2.32/8.4.24 WITH DOM;1304withoutDOM
(HTML not run).76PHPfiles lint.84baseline hashes/6original regression files
unchanged. New review suite131checks DOM/128without; officialWPCLI86/84checks,
actual facade-dispatch local archive/bindings file and booleans tested. During
implementation missing option description made official DocParser consume next
option; fixed synopsis then reran clean. File-vs-demo plan equality test corrected:
canonical manifest/candidates equal while different input byte serialization
correctly has distinct input hash/plan. Null binding rejected strictly.

PASS164native MySQL8.4.13 checks on final code (146previous +18archive bridge).
Actual7schema definitions/InnoDB + two synthetic legacy tables, WP/wpdb adapter
stubs. Bridge2doc case exactly4SELECTs(identity,2bindings,snapshot), no insert;
6citations and9gaps, native current equal-value/hash drift, blocked source, all9
synthetic table row hashes preserved. Prior transaction/rollback/ackloss/dedupe/
contention/review regressions rerun. Two own temporary containers created/removed,
1CPU/1GiB/512MiBtmpfs, isolatedloopback, no userLocalWP/VPS/realdata. Earlier run
at qa/dev7.8 root, finalcode at qa/dev7.8/native-final. Existing standing operator
approval for disposable syntheticMySQL reused; no new source request permission
assumed. No credentials/config printed or userwp-config access.

NOT TESTED newinspect on realWordPress/userLocalWP/production/VPS load or actual
source facts;39WPchecks dev7.6 remain prior-version evidence. Plan reads no locks,
not a persisted/durable transaction or cryptographic provenance. Snapshot only
verified meta does not assess every legacy field.9topic gaps not absence claims.
Raw pending storage and binding, retention/privacy policy, actual source/identity
attestation, positive approval, lease/fenced durable worker and publisher/undo
remain unfinished; no false MVP-complete/200enriched/ranking/AI recommendation.

Docs ARCHIVE_REVIEW.md Windows example; worker scope/order unchanged. No new
schema/options/roles/hooks/network/writes defaults. Rollback files to7.7, no DB
migration; preserve all old data/audits/operatorarchives. Access policy refreshed
restricted/enforced/custom0; no govt probes, remaining research18/20first10 only.
Next safe work: raw-pending durable storage contract with guarded explicit write
and atomic failure tests, then approval/worker/publisher gates. Package7.8 + guide
via GitHub newbranch per standing user permission, main/oldartifacts preserved.

Dev.7.8 ZIP+guide pushed; remote ref verified 57b147eef2aaead1c058940279d165d817c815d3 (delivery/archive-review-dev7.8). Only2new artifacts; main/earlier packages preserved. No actual school facts enriched. Source/ZIP immutable release contents verified before delivery.

## 2026-11-10 — user LocalWP inspect receipt + dev.7.9 raw archive vault

USER-REPORTED PASS read-only7.8 demo: `pilot inspect --demo --npsn=20210711
--dry-run`, school_id339909,2docs/3candidates/6evidence,3article sections/9gaps,
errors/conflicts empty. All write/network0 and store/approval/publishfalse. Correct
fixture/stale/missingbinding blockers. Parsed full uploaded28KBlog, no new error
observed; raw original SHA in docs/qa/localwp-inspect-demo-user-report.json. User
exit code not supplied. This validates reported native LocalWP demo output only,
not real source/storage/publisher or cloud-run test. Don't repeat the old demo.

DONE dev7.9: ADE_Archive_Vault, TYPE m2_raw_archive_pending, one explicit raw-only
archive row in existing Discovery jobs. Localcap/actor/preflight gates; defaultOFF
ADE_LOCAL_ARCHIVE_STORAGE_ENABLED, stage token+STORE_RAW_PENDING+backupYES+
privacyYES required. Stage read-only. Reject fixture/stale/mismatch/conflict/error
and missingblocked source bindings. Raw selectedschool <=3docs plus extraction
trace/current snapshots, source/fullinput/manifest hashes, actor/time/privacy and
noattestation/noapproval flags. Full encoded envelope <=1MiB; excludes raw199other
schools. No schema migration, profile/evidence/candidate/link/source/review writes.
No network/frontend/cron/autoload/roles/options. No real source data acquired.

Atomic transaction INSERT onejobsrow, shared M2/M3 GET_LOCK0 perprefix+school,
source/relation NOWAIT recheck IDs/canonicalkey/URL/host/status; locked receipt.
Fresh context/plan compared to token; insert/commiterror rollback; finallyrelease.
Operationkey binds frozen scope/fullmanifest/school/selectedbundle. Sameactor exact
retry historicalreceipt rows0; otheractor write replay blocked. Lost COMMITack
recoverable from persisted receipt. Receipt command validates cappedraw bytehash,
selectedschool metadata and summary, outputs metadata only (never rawHTML/token).
Application doesn't UPDATE rawrecords; revisions distinct. Checksum is integrity,
not cryptographic source attestation or protection against a DBadmin rewriting
payload+summary. Retention/export/delete/encryption/quota-total NOT IMPLEMENTED;
privacyYES only operator acknowledgment, not automatic PII/secret scanning.

Commands `vault_stage`, `vault_store`, `vault_receipt` use underscores; actual
WPCLI2.12 parser/dispatcher checks flag synopsis and defaultOFF before file read.
Do not run actual LocalWP writer yet: no authorized real-source plan/backup/write
approval. Cloud syntheticMySQL standing permission reused, not userdatabase consent.
ArchiveReview blocker renamed ARCHIVE_EVIDENCE_CANDIDATE_STORE_NOT_IMPLEMENTED:
rawstorage now exists but receipt->evidence/candidate bridge does not. Existing
inspect still read-only and flags storage false for candidate workflow.

PASS23offline suites1416checks each PHP8.2.32/8.4.24 WITH DOM;1348withoutDOM
(HTML not run).78PHPfiles lint.37vault assertionsDOM/36without (encodedlargeHTML
cap not run withoutDOM),94officialdispatcher DOM/92without. Baseline84hashes and
6original regressions unchanged. Include check selection other199 as one invariant,
not inflated per-school test count. Fake transaction tests cover defaultOFF,
fixture/stale/binding/consent, current/source-lockrace, sizebound, exactretry,
receipt/tamper/otheractor, insert/COMMIT failure and commitackloss recovery.

PASS195actual MySQL8.4.13 checks (164previous +31vault), WP/wpdb adapter stubs.
Native raw1row, receipt2docmetadata, no evidencecandidate writes, dedupe, insertion
rollback, actual2session mutex/NOWAIT (<2s), stale snapshot, durableCOMMIT with
simulated ackloss, tamper/restore bytehash, all8nonjobs synthetic table hashes
preserved. Existing transaction/review regressions rerun. Oneowncontainer created,
1CPU/1GiB/512MiBtmpfs, loopback ephemeralport, removedfinally; no real DB/site used.
Runtime/native script hashes captured, qa/dev7.9 log/native-mysql-result.json.

NOT TESTED7.9 rawwriter with actual WordPress/wpdb/userLocalWP/real facts/production,
privacy automated scanner, encryption/retention/quota, native forceddiskfailure or
trueTCPcommitackloss.39actualWPchecks dev7.6 prior scope; user7.8demo separate above.
Captured snapshots are informational, not serializable lock on legacy editors;
futurecandidate/publisher must recheck. No reviewed candidate/evidence touched.
No200factualprofiles/SEO/AI promises; only3literalfields supported and9topic gaps.

Docs RAW_ARCHIVE_VAULT.md, oldread-only docs get version-scoped7.9note. Rollback
pluginfiles to7.8, no migration/delete/import; any explicitly created rawreceipt
must be retained. Currentuser data unchanged, flagsOFF. Networkstatus refreshed
restricted/enforced/custom0; no govtprobes or bypass, researchstill18/20first10.
Next: consent-gated receipt->evidence/candidate bridge preserving raw bindings,
reviewedstates and transaction receipts, then lease/fenced worker/positive approval/
publisher/undo. Deliver7.9 ZIP+guide via newGitHubbranch under standing permission.

Dev.7.9 ZIP+guide pushed; remote ref verified 653f2138c6d0580fdce54f6c01adacff199a320f (delivery/raw-vault-dev7.9). Only2new artifacts; main/earlier packages preserved. No actual school facts enriched. Source/ZIP immutable release contents verified before delivery.

## 2026-11-10 — dev.7.10 raw receipt -> pending evidence/candidates

DONE defaultOFF ADE_Archive_Candidates / TYPE m2_archive_candidates. Existing raw
receipt ID + matching frozenNPSN only. Guarded internal Vault::for_candidates
validates capped receipt/hash/school, reparses stored selectedraw and rechecks live
identity/classification/current verified meta/source bindings. Captured extraction
ignored (forged derivedcapture test confirms raw used). Shared Vault lock_sources
helper extracted, canonicalID/key/URL/host/status NOWAIT unchanged. Manual
EnrichmentStore runtime unchanged byte-for-byte from7.9; new writer separate.

CLI archive_stage(read-only strictdryrun), archive_store(opt-in, explicit
STORE_ARCHIVE_CANDIDATES/backupYES/fresh token), archive_receipt(historical).
ADE_LOCAL_ARCHIVE_CANDIDATES_ENABLED undefined/OFF independently of rawvault flag.
No user LocalWP write/enable/config edits authorized or executed. Guarded localCLI,
ade_manage_jobs+ade_review_candidates+positiveactor, not new webPOST/nonce path.

Atomic Discovery candidates/evidence/candidate_evidence/jobs only. Three field
allowlist preserved. Same candidate dedupe as manualM2; pending reuse, no proposed/
snapshot overwrite. Distinct raw/source evidence keys carry rawreceiptID/rawpayload
SHA, documentkey/rawdocSHA/format/archiveevidencekey. Parse m2_archive_unverified,
identity pending/permissionNOT_INDEPENDENTLY_VERIFIED. New candidates new/not_ready,
score0/approvedNULL. Reviewed/approved/published/approvalmarked frozen, no hidden
links appended. New pending links advance row_version CAS. Same M2/M3/rawmutex,
raw/source/candidate/evidence/link/operationreceipt NOWAIT row locks, fresh snapshot
and actor-bound plan token, short transaction, all-or-nothing receipt+rows, retries
historical/deduped; commitackloss recoverable. No profile/source/reviews mutations.

Two-doc example:3candidate+6evidence+6links+receipt=16rows beyond existingraw.
Reuse3manualpending ->13newrows +3versionadvances; after1reject,9rows +2advances.
Source IDs from two hosts retained (7/9 in syntheticnative). Rawblob unchanged.
Inspector accepts new parse status, validates proof metadata shape and displays
rawreceipt/format/docSHA with escaping. RAW_ARCHIVE_BINDING_NOT_REVALIDATED_ON_THIS_PAGE
explicit: UI doesn't load upto20rawpayloads of1MiB each; pointer/recorded hash only,
not raw revalidation/source verification/approval. All decision/publication defaults
unchanged OFF; full verification still needed before futurepositive approval.

PASS24offline suites1504checks per PHP8.2.32/8.4.24 WITH DOM;1436withoutDOM
(HTML NOT RUN).81PHP lint,84baseline hashes/6original regressions preserved.
Newbridge77fakeDB assertions incl16insert positions atomic rollback, pendingCAS,
raw/current/source-race, actor/IDOR/consent, twohostmapping, manualpendingreuse,
reviewedfreeze, ignore forged derivedcapture. Shared fake StoreDB moved to support,
original115manual regression checks retained; initial adapter failure surfaced
stale nested last_error, fixed test wrapper clearing like wpdb, suites rerun clean.
100officialWPCLI dispatcher checksDOM/98without, actual disabled handler reached
before DBaccess; command underscore names and valid synopsis, strictflags.

PASS282actualMySQL8.4.13 checks (195prior+87bridge), WP/wpdb adapterstubs, actual
schema7tables, syntheticdisposable DB. Native16row/receipt, sixrawbound evidence,
twohosts/sourceIDs, IDOR, all16insert-failure rollback/rawpreservation, actualCOMMIT
with simulated ackloss/replay, revisionappend/reviewedfreeze, real2session mutex/
secondsourceNOWAIT(<2s), stalesnapshot;5protected synthetic table hashes unchanged
(schools/meta/sources/relations/reviews). Twoowncontainers (initial and final runs, nonconcurrent)1CPU/1GiB/512MiBtmpfs,
loopback ephemeral, removedfinally. No userDB/config/source/production access.

PASS26Chromium checks (actual PHPview + fixtureWordPress/DB/minimalCSS, not fullWP):
GETnavigation/filters, defaultnoPOST, opt-in negative forms unchanged, XSS,403,
empty/conflict, rawpointer/no false revalidation, longhashmobile wrapping, no
externalrequests/pageerrors. Newmobile screenshot manually inspected; comparison
table retains bounded horizontal scroll as before. Ownserver stopped. QA proofs
in docs/qa/dev7.10/browser and native/offline logs. Prior39actualWPchecks7.6 and
user7.8inspectreport retain their historical scope; not relabelled newwriterPASS.

LIMITS: newwriter actualWordPress/wpdb/userLocalWP/realdata/VPSload NOT TESTED.
Raw/metadata hashes are integrity checks not signatures or DBadmin protection;
legacy editor reads not serializable apply-lock, publisher must recheck. No
positiveapproval/sourcepermission/identityattestation/durableleaseworker/publisher/
postcommitundo. Rawprivacy/retention/export/encryption/totalquota7.9 outstanding,
no real writes until policy and concrete operator approval. No sourcefacts acquired
or200completearticles/ranking/AI promises. Only3literalfields and9unassessedtopics.

Docs ARCHIVE_CANDIDATES.md, olddocs version notes, source/QA/diff packaging. Rollback
files to7.9 no schema migration; retain all data/receipts. After any futureactual
write,7.9inspector may block unfamiliar archiveevidence, so plan compatibilitybefore
rollback. ActualuserDB unchanged and flagsOFF. Cloudpolicy refreshedrestricted/
enforced/custom0; no govtprobes/bypass, remainingresearch18/20first10 only. Next:
fullWordPress integration bridge+inspector, positive review rawbindingvalidation/
sourceattestation, then lease/fencing worker and publisher locally with approval.
Deliver7.10 ZIP+guide on newGitHubbranch under standingpermission; no mainmerge.

Final7.10 review added encoded metadata/result16KiB cap before operationreceipt insert. LongUnicodeURLs test proves rollback of all partial claims when cap exceeded. Finaloffline1504/1436 and bridge77checks; native282final rerun on new owncontainer (removed) at docs/qa/dev7.10/native-final; initial282proof retained with original scope. No runtime changes after final run.

Dev.7.10 ZIP+guide pushed; remote ref verified e038a3f31f919039084a68f68b004eb95b24f47d (delivery/archive-candidates-dev7.10). Only2new artifacts; main/earlier packages preserved. No actual school facts enriched. Source/ZIP immutable release contents verified before delivery.

## 2026-11-10 — user-authorized GitHub artifact cleanup

Removed28superseded ZIP/guide files from active delivery tree and14obsolete remote delivery branches. Kept only dev7.10 ZIP+updated guide in delivery/archive-candidates-dev7.10, and main2contract documents unchanged. Active commit 1fea72830999e8d32adb331786e73722a4091430. LatestZIP SHA unchanged 576276dc9715be4aa5c139bd59c5e8e3b400ec6382df7a44001d8d94d8a4bf96. Visible artifact bytes16,602,685 ->3,354,374; this is file-tree size, NOT actual GitHub storage reclaimed. Normal child commit, no history rewrite; old objects still reachable via commit ancestry. Verified local backup bundle /workspace/ahda-backups/github-before-cleanup-2026-11-10.bundle and ref manifest. Atomic leased push guarded all expected old SHAs; final remote heads exactlymain/currentdelivery. Local source/baseline/olderpackages preserved for QA/recovery. Guide rollback now uses local backup, warns historical branch links may no longer work. No plugin code/site/database changes. Evidence docs/qa/github-cleanup-2026-11-10.

Future delivery policy from user: keep only newest ZIP+its guide in active GitHub delivery tree; do not re-add all historical artifacts via old read-tree snapshots. Keep baseline/olderQA packages locally or backup bundle for regression/rollback. Use current active tip as parent; archive/remove superseded remote delivery branches after verifying backup, and retain main contracts. No forced history rewrite authorized.

## 2026-11-10 — progress estimate and dev.7.11 actual WordPress bridge integration

Operator asked percentage + continue to completion. Answered ~55% code foundation,
qualitative milestone estimate, NOT measured test/overall success ratio. Real
school factual enrichment0/200. Added docs/MVP_ACCEPTANCE.md with concrete gates;
do not increase percentage just from test counts or claim ranking/AI/100%secure.

DONE: extend owned actualWordPress7.1.4/Directory0.8.9/MySQL8.4.13 harness for
raw->candidate APIs and realadmin display. Plugin runtime compared to7.10: header/
version7.11 only. No source fetch/new mutator, all actual-user flagsOFF. New
bridge-pipeline.php called only after ownedCLIbootstrap, explicit syntheticmarker.
Uses actualwpdb/capabilities/users, no database/core API replacement. A presence-only
WP_CLI class marker satisfies CLI guard; these are service API tests, NOT complete
official WP-CLI runner/dispatcher. Existing officialdispatcher offline tests remain.

PASS final83service checks actualWordPress/wpdb: actual admin/editor pluginroles,
rawstage readonly/defaultOFF/insert/hashreceipt/replay, candidate defaultOFF,
IDOR/token/backup/confirm, each16insert positions intentionally rejected through
actualWP queryfilter+realMySQL syntaxerror, all7Discovery row hashes rolled back,
3newcandidate/6evidence/6links/1receipt exactly, rawimmutable, twohosts/sourceID7/9,
actualInspector rawpointers/revalidationnotice, noapproval/score/publication,
receipt/idempotence, rawrevisionpendingreuse13rowplan, priorreviewfixturestale,
reviewedrow/linkfreeze9rows/2versions. Original3seededcandidate/evidence/links
and source/relation/audit records preserved. Prior-review fixture status was
controlledsyntheticSQLsetup; actualauthenticatedHTTPnegativeflow testedseparately.

PASS47realbrowser/adminWordPress checks (39previous+8new) actuallogin/roles/cookies/
nonces/admin-post, invalidaction/session/CSRF/IDOR/stale403/409, defaultOFF+testON+
OFF, negativeaudit/replay/escaping, realnewarchivepointer/data, rawhash wrapping/
mobile/noPOST, all25actualDirectory legacy synthetic table row hashes unchanged,
allapprovedNULL/publishnot_ready. No externalbrowserrequest, latestscreenshot
manuallyinspected, sourceURLs only example.org/net metadata. Core source pinned
SHA db96f5eaa77a8d3e8eec8923a518fa2326f0d46a unchanged. Testwp-loadshim/homealias
and loopbackRESTscope explicit, no wp-config file read/generated/modified.

Initialrun83+47functionalPASS had3Coreupdatecheck warnings due to deniedtestHTTP.
Initial evidence retained wordpress-attempt-1. Testbootstrap then removes Core
adminupdatecheck/schedulingcallbacks only inside ownedsite; user/Core cache not
changed. Finalrun83+47PASS with runner enforce zeroPHPwarning/notice/deprecated/
fatal. Allmail/HTTP/cron/updaters denied in test; no TLSdisabled or policybypass.
TwoownDBcontainers/sites/servers (initial/final, nonconcurrent) removedfinally,
1CPU/1GiB/512MiBtmpfs/loopbackephemeral. Test opt-ins onlyoneCLIprocess, subsequent
HTTP OFF. Passwords/salts/cookies/nonces not saved to QA artifacts. Evidence
qa/dev7.11/wordpress/*.json/logs/screenshots; finalphp_diagnostics_clean=true.

Offline24suites1504checks eachPHP8.2.32/8.4.24 WITH DOM,1436without (HTML NOT RUN),
82PHP lint (newguardedbridge testscript),84baseline hashes/6original regressions
unchanged. Native282underWPstubs and26fixturebrowser are prior7.10 evidence, NOT
rerun/relabelled; finalnewactualWP scope above. No actualuserLocalWP/end-to-end
WPCLIrunner/theme3rdparty/VPSload/TCPcommitfail/sourcefacts/positiveapproval/publisher
validation. Sourcepermissions/rawfullreview/retention/leaseworker/publishergates
still outstanding, 0/200 factual profiles unchanged. FullWordPress service gate
now has concrete evidence; no claimallMVPcomplete or increase55%solelybecause tests.

Docs WORDPRESS_ARCHIVE_BRIDGE.md + MVP_ACCEPTANCE.md + harness README, source/QA
package7.11. Rollback uses user's localbackup; no schema/delete/import. UserGitHub
policy: only latestZIP+guide active, remove supersededremote deliverybranch with
localbackup/leases, preserve main2contracts/history, no forcedrewrite. Parentmust
be cleaned7.10 tip1fea72830999e8d32adb331786e73722a4091430, do notre-add old28files.
Cloudnetworkstatus refreshed enforced/custom0; no govtprobes, research18/20first10.
Nextsafe implementation: full raw-binding verifier in review + explicit source/
identity/permission attestations, positiveapproval, durableworkerlease/fencing,
then publisher/undo locally with scopedoperatorapproval. Keepproductionexcluded.

Dev7.11 ZIP+guide delivered to refs/heads/delivery/wp-bridge-dev7.11 at d46bc5e2b58867983d3871591861c6237bc50389. Atomic create/current-replacement+delete superseded7.10remote, active artifact tree exactly2files. Main unchanged; no historyrewrite, localbundle /workspace/ahda-backups/github-before-dev7.11-delivery.bundle. Finalrelease bytes match83service/47browser WordPress proof and packagedoffline1504/1436 tests. Runtime7.10 behavior preserved; actualprofile enrichment remains0/200 and estimated foundation~55%.

## 2026-11-10 — dev.7.12 explicit one-evidence raw verifier

DONE ADE_Archive_Verifier + CLI `pilot archive_verify` strictdryrun, matching
storedcandidate/evidence IDs/NPSN only. New Vault::verification_archive internal
read API requires reviewer/actor/local/preflight, no CLI marker requirement. No
rawbody/quote/value/authorizationtoken returned or cached, no new endpoint/cron/
page-load work. Writer/review/publisher runtime logic unchanged, opt-insOFF.
Candidate/source/raw/profile data is never mutated by verifier.

Prepared bounded supportlink/candidate/evidence join same-school, allowlisted
3targets/types/status, NULL/bytecaps, strictproof JSON+duplicatekeys, rawreceipt
ID/hash/schema/school validation then freshparse (ignorescaptured extraction).
Compare exact quote/value/target/rawdocSHA/format/sourceURL/normalizedfingerprint/
checkedtime/archivekey + recomputed stored evidence_key. Recheck registeredsource
ID/host/relation/pendingpolicy. Current verifiedmeta/basehash conflict reported;
second pairread rejects rowversion/data drift. snapshot_only / must_revalidate_for_
approval true, no transaction lock/signature/trustpromotion. identity/permission/
approval/publication false even DB officialverifiedlabel. Stale/conflict blockers
preserved; manual evidence without rawbridge cannot masquerade as rawverified.

PASS25offline suites1545checks perPHP8.2.32/8.4.24 WITH DOM;1477withoutDOM (HTML NOT
RUN),85PHP lint.84baseline hashes/6original regressions intact. New38fakeDB checks
raw/quote/value/fingerprint/date/source/proof tamper, null, duplicateJSON, gate/
IDOR/readfailure, midcheckversiondrift, currentconflict/rejectedunchanged, no writes.
OfficialWPCLI103checksDOM/101without, synopsis/requiredtrue dryrun validated. Shared
ArchiveDB fakeclass extracted to support, sourcequery shape adapted; initial
attribute tamper test changed a field to samevalue, fixed to protecteddifferent
field; nullable fake OCTET_LENGTH adapter fixed (test deprecation), finalclean.

ActualWordPress7.1.4/Directory0.8.9/wpdb/MySQL8.4.13 finalPASS96service+47browser,
newverifier covers6storedtwohostproofs/metadata pointer only, actualquote/SHA/
sourceblock/role/IDOR negatives, no7Discovery mutation after restore;25legacy
synthetic tables hashes unchanged. Existingbridge16insertrollback, reuse/review
freeze/rawimmutable/replay, actualauth/nonces/admin-post retained. Directservice
API with explicit class-presenceCLI marker for pre-existingwriteharness, not an
end-to-end officialWPCLIrunner. No core/db/capability function replacement.

Attempt1 FAILED login waitForURL30s before bridge; allownresources removed. Cause
not established: oldharness lackedlogin/server diagnostics. Added safe failure
pathname/origin/error_text (no password/cookie/nonce) and redactedHTTPserverlog.
Attempts2and3 freshowned sites bothPASS96+47 with cleanPHPdiagnostics; no timeout
increase, no hidingfailedinitialrun. All3ownDB/site/server removedfinally,
1CPU/1GiB/512MiBtmpfs/loopback. InitialFAIL retained qa/dev7.12/wordpress-attempt-1,
priorPASS attempt-2, finalwordpress. Corecache unchanged; no userwp-config touched.
Initiallogin flakiness rootcause remains known test limitation; not userLocalWP
FAIL/production readiness. BrowserUI unchanged; per-page rawpointer still honestly
NOT revalidated there. Verificationreport from explicit CLI is fresh ephemeral.

LIMITS: no sourceidentity/permissionattestation, positiveapproval/durableworker/
publisher/undo, rawprivacyretention/encryption/quotatotal; source/raw/meta may change
after check, futureapproval must revalidate under locks. DBadmin can rehash own
payload; checksums are integrity only. OfficialCLIrunner/userLocalWP/thirdparty/VPS
load/TCPcommitfailure untested. No sourcefacts/publication or realuserDB write.
Estimatefoundation~55%not measured, realenrichment0/200; don't inflate by testcount.

Docs RAW_BINDING_CHECK.md/readme/checkpoint, no schema/role/options/migration.
Rollback files7.11 no dataundo/delete/import. Preservelatest-only GitHubZIP+guide,
parent d46bc5e2b58867983d3871591861c6237bc50389; backup/delete oldremotebranch via
atomicleases, main2contracts untouched, no forcedhistoryrewrite. LocalolderQA ZIPs
retained. Networkstatus enforced/custom0; no govtprobes or bypass, still18/20first10.
Next: explicit identity/permission/source attestation model and positiveapproval
using fresh raw verifier, then durableleaseworker/publisher localwithoperatorconsent.

Dev7.12 ZIP+guide delivered to refs/heads/delivery/raw-check-dev7.12 at 984805553df0f7017e93d852f90c83ae5300720e. Atomic create/current-replacement+delete superseded7.11remote, active artifact tree exactly2files. Main unchanged; no historyrewrite, localbundle /workspace/ahda-backups/github-before-dev7.12-delivery.bundle. Finalrelease bytes match96service/47browser WordPress proof and packagedoffline1545/1477 tests. Existingwriters/review/publication defaultsOFF; actualprofile enrichment remains0/200 and estimated foundation~55%.

## 2026-11-10 — dev.7.13 operator source statements + append-only withdrawal

DONE ADE_Source_Attestation, defaultOFF ADE_LOCAL_SOURCE_ATTESTATION_ENABLED.
One claim/candidate/evidence/raw/source-bound **operator declaration**, never
independentverification/sourcebadge/approval. Strict16KiBJSON request, identity
basisregistry_crosscheck/school_confirmation + reference + note40..500including
NPSN/host; permissionbasisexplicit_permission/open_license only, ref+note, allthree
identity/permission/privacy booleans true; UTC expiry>60s/<=90days. References are
metadata/humanreview, not fetched or proven authentic. Fixed scope one_short_
factual_claim_with_attribution excludes raw/crawl/wholearticle/images/PII rights.

CLI attest_stage(read-only), attest_record(flag/backupYES/token/confirm), status,
attest_revoke_stage/revoke. No new webroute/form; CLIwriter managejobs+reviewcap/
actor/local/preflight, readstatusreviewcap/local. Source/relationship/identitylabel/
profile/candidate/evidence/reviews unchanged; one append-onlyjobsrow pergrant or
withdrawal acts as audit+receipt. No migration/role/options/schema change. No
realuserwrite/enable/sourcefetch/config/production operation.

Grant binds fresh verifier/raw/content/source-state, actor/notes/refs/expiry, candidate
version in plan. Revocation bound to grantID+operation, explicitreason/note/actor,
possible even when source blocked/raw check fails/expired. Currentstatus false on
revoked/expired/source-binding-current drift, no rewriting oldevents. Samegrant
retry historical, no duplicate; revoke differingactor/reason doesn'toverwrite.
Regrant is new explicitoperator declaration, not domainwide permission/ban.
No postcommit deletion/undo/publication withdrawal implemented; futurepublisher
must handle revocations before apply. Human statement isn't legal/ownershipproof.

Late security review fixed RR stale-snapshot risk: attestationwrite context invokes
internalverifier locked CURRENT reads from firstcandidate/evidence SELECT, then
raw/source/secondpair locks NOWAIT. Vault verification_archive and verifier gain
optional internal lock arg; CLI/read default remains lockfree snapshot. Scope
writes retain same M2/M3/raw schoolmutex. Native2wpdb session test establishes RR
snapshot inmainconnection, secondsession increments candidateversion, firstlocking
read must observeincrement and reject stale token. Actualfixture restoredexactly.
Existinglegacy meta consistentread NOT serializable applylock; publisherfuture
must lock/recheck. Sourcecurrent()reader is snapshot only; **positiveapproval must
add locked grant+revocation validation API**, never authorize from oldstatusreport.

PASS26offline suites1588checks eachPHP8.2.32/8.4.24 WITH DOM,1520withoutDOM (HTML
NOT RUN),88PHP lint,84baseline hashes/6original regressions intact. New35fakeDB
checks inputscope/referenceflags, expiry/historicalexpired, consentOFF, immutable
states/replay, corruption, rollback/lostack, blockedsourcewithdrawal, staleversion,
mutex/capability. VerifyDB class extracted to support for reuse, no runtime DB
adapter replaced. Existing manual/archive writers and negative review unchanged.

PASS118actualWordPress7.1.4/Directory0.8.9/wpdb/MySQL8.4.13 services +47realbrowser/
admin checks. Statement readonly/defaultOFF, actualeditor denied, actualINSERT/
COMMIT errors through Core queryfilter roll back, grantcurrent/nonindependence,
replay, sourceblocked invalidation, withdrawal/replay afterblocked, all6nonjobs
Discovery and25synthetic legacy tables unchanged. New2session RR regression above.
Direct service API with explicitWP_CLIclass-presence marker, NOT officialrunner;
no SQL/core APIstubs. FinalPHP diagnostics clean, no externalbrowserrequest.
Twoowncontainer/site/server runs (116initialpre-hardening,118final, nonconcurrent)
removedfinally. Evidence qa/dev7.13/wordpress-before-current-read and finalwordpress;
sourcecache pinned/unchanged, no wp-config read/generated. InitialPASS not relabelled
as finalcurrent-read proof. Existing7.12login-timeout limitation kept inpriorlogs.

Source/declaration authenticity/permission conditions still human responsibility;
no positiveapproval/edit/publisher/undo/durableleaseworker/rawretention/encryption/
totalquota yet. No completeofficialCLIrunner/userLocalWP/thirdparty/VPSload/genuine
TCPcommitfailure test. Corruptgrant or expired/blocked check failsclosed; DBadmin
rewriting allhashes not prevented by checksum. No factualenrichment0/200; foundation
estimate~55% remains qualitative, don't inflate from testcounts. Next add locked
attestation/revocation check and positiveapproval transaction, then durableworker/
publisherlocal with scopedactualoperatorbackup/consent. Productionexcluded.

Docs SOURCE_ATTESTATION.md/readme/checkpoint. Rollback files7.12 no migration,
keep alllegitdata/events, no deletion/import. Latest-only GitHubZIP+guide policy:
parent984805553df0f7017e93d852f90c83ae5300720e; localbundle then atomiccreate/new
pair+delete supersededremote, main2contracts/history preserved. Cloudpolicyenforced/
custom0 no govtprobes/bypass, standingresearch18/20first10 unchanged.

Dev7.13 ZIP+guide delivered to refs/heads/delivery/source-attest-dev7.13 at 90331677e59a6559ef47a8942e7f02932b5a6726. Atomic create/current-replacement+delete superseded7.12remote, active artifact tree exactly2files. Main unchanged; no historyrewrite, localbundle /workspace/ahda-backups/github-before-dev7.13-delivery.bundle. Finalrelease bytes match118service/47browser WordPress proof and packagedoffline1588/1520 tests. Existingwriters/review/publication defaultsOFF; actualprofile enrichment remains0/200 and estimated foundation~55%.

## 2026-11-10 — dev.7.14 one-claim positive review, local CLI/service only

DONE ADE_Positive_Review plus approve_stage/approve_record. Default OFF constant
ADE_LOCAL_POSITIVE_REVIEW_ENABLED; no positive web form/handler, no automatic or
bulk/edit approval. Same three allowed text fields only. Operator declaration is
not independent verification; source labels/identity/score/badge remain unchanged.
No real-user enable/write, source HTTP, wp-config, migration/import/delete or
production operation. Factual enrichment remains0/200; ~55% foundation estimate
remains qualitative, not inflated by tests.

Read-only preview rechecks raw + operator grant and displays one proposed value,
version, target/status and actor-bound token. Strict7-field CLI JSON <=8KiB; write
requires explicit APPROVE_ONE_CLAIM and backupYES, local managejobs/CLI guard and
review capability. CLI creates a nonce for its authenticated operator only after
these guards. Service also requires nonce, explicit confirm/backup; future web
must supply submitted nonce. Notes10..500 UTF8bytes, rejectHTML/control/bidi;
request field order normalized, values cannot be edited during approval.

New internal Source_Attestation::approval_context exact school/candidate/evidence
match; locks grant and potential unique-key withdrawal receipt, fresh raw/source
binding, expiry >5seconds, candidate version. Readmode transient only. Locked mode
requires caller transaction+sharedschoolmutex; PositiveReview owns both. Existing
verifier lockmode now also CURRENT-locks legacy verified target SELECT (read only),
so stale RR snapshot can't hide basehash conflict. No legacy writes. Existing
raw verifier standalone historical POSITIVE_REVIEW_NOT_IMPLEMENTED blocker still
refers to its own non-approval route; not an authorization API. Keeping output
preserves old declaration binding hashes. UI wording scopes unavailable approval
to that page; UI does not automatically parse raw or offer positive submit yet.

Atomic Discovery-only transaction: CURRENT reads/NOWAIT grant/revoke/raw/candidate/
evidence/link/source/legacytarget, token/version/state check, candidate CAS sets
approved_value=unchanged proposed, approvedreviewer/time,rowversion+1; publishstatus
staysnot_ready/publishedtimeNULL. Append reviews audit with exactvalue, actor/note,
declaration/hash/expiry and versions; appendjobsreceipt m3_positive_review. Every
write failure/commiterror rollsback; exactretry validates bounded receipt and full
bounded audit, returns historical/write0. Approved candidates immutable. Grant
withdrawal after approval preserves historicaldecision; futurepublisher MUST
fresh-lock/recheck permission/raw/basehash, never trust oldapproved status/receipt.
No undo/delete/resetapproved fields implemented. ChecksumsnotDBadmin signatures.

PASS26offline suites1597checks eachPHP8.2.32+8.4.24 DOM;1529withoutDOM (HTML NOT RUN);
89PHP lint each;84baselinefilehashes/6originalregressionfiles intact. OfficialWPCLI
2.12 parser/dispatchertests validate newcommandPHPDocs/OFF/dryrun; no officialfull
runner E2E. Fakeattestationtests now40 inclapprovalcontext scope/revoked/expired/
blocked source. NewpositiveSQL state machine tested with actualwpdb, not fakeSQL.

PASS actualWordPress7.1.4/Directory0.8.9/MySQL8.4.13:151servicechecks+47browserchecks.
PositiveOFF/readonly/capability/nonce/confirm/backup/XSSinput/strictkeys/schoolscope,
withdrawalafterpreview, UPDATE/auditINSERT/receiptINSERT/COMMIT failures + exact
rollback hashes, two-sessioncandidateRRrace, success3writes/approvednotpublished,
exactretry, immutableapprovedvalue, postapprovalwithdrawal/history checked.
Second-session syntheticrevocation inserted after mainRR snapshot BEFORE first
lockingreceiptread; grant/revocation CURRENT reads must see withdrawal and reject.
This intentionally noncooperating SQLfixture isn't a sourcegrant or real permission.
All25legacyhashes and sources/relations/evidence/links unchanged by positive review.
Browser47 rechecks actualadmin/login/nonce/negativeflow and pendingviewer; final
snapshot asserts only explicitly approved syntheticcandidate has approvedvalue,
allpublishstatusesnot_ready. No positive webform/browseraction claimed.

Twoownsites/containers/servers (149initial+47browser beforefinalreview,151final+47)
removedfinally, cleanPHPlogs, no wp-config generated/read, corecache unchanged.
Proof docs/qa/dev7.14/wordpress-before-final-review vs finalwordpress; retain their
scope and do not relabel initialproof as final. No actualuser LocalWP, thirdparty
source, VPSload, fullofficialCLIrunner or genuineTCPcommitackloss E2E tests.
Faultinjection COMMIT test rejects beforecommit; exactretry tested aftersuccess.

Next: positive admin form with capability+submittednonce and explicit oneclaim
preview/confirmation, then durableextraction leaseworker and controlledlocal
publisher/rollback. Rawprivacy/retention/encryption/totalquota and realrights/source
collection remain gates. No site or article SEO/ranking acceptance yet.
Rollback files7.13 usinglocalbackup, no schema migration or data deletion; retain
approved/audit/event history. Networkpolicy customhosts0 (no govtprobes, remaining
researchbudget18/20first10 unchanged). Deliverylatest-only ZIP+guide with guarded
atomic create+remove oldremote, preservemain/history, localbundle first. Parent
90331677e59a6559ef47a8942e7f02932b5a6726.

Dev7.14 ZIP+guide delivered to refs/heads/delivery/approve-dev7.14 at 0ac151473dfd8eec741ecb17b60ca72662236189. Atomic create/current-replacement+delete superseded7.13remote, active artifact tree exactly2files. Main unchanged; no historyrewrite, localbundle /workspace/ahda-backups/github-before-dev7.14-delivery.bundle. Finalrelease bytes match151service/47browser WordPress proof and packagedoffline1597/1529 tests. Existingwriters/review/publication defaultsOFF; actualprofile enrichment remains0/200 and estimated foundation~55%.

## dev.7.15 IN_PROGRESS checkpoint after session time limit

Code implemented: admin/class-ade-admin-approval.php two-stage POST preview/apply,
source declaration scoped metadata read without raw reparse, positive history,
admin integration/defaultOFF, HTTP synthetic fixture/metrics/browser checks.
Offline PASS1599/1531 checks eachPHP8.2/8.4 DOM/noDOM,91lint,84baseline/6regressions.
Initial actualWP PASS151service/88browser at qa/dev7.15/wordpress-before-final-review.
Subsequent final-review run FAILED during second admin login (30s timeout, no login
POST after third login page GET in serverlog; cause unproven). Retained failure at
qa/dev7.15/wordpress; all own resources cleaned. Do not claim final code WP PASS yet.
Docs ADMIN_APPROVAL.md drafted. Next diagnose test login race, rerun final WP,
package only current QA to reduce disk/ZIP, write final checkpoint and deliver
new latest-only GitHub pair (current remote approve-dev7.14 at0ac151473dfd8eec741ecb17b60ca72662236189).
No userDB/network/production operations. Actualfacts0/200, flags OFF, no publisher.

## 2026-11-10 — dev.7.15 DONE: admin positive approval and lean installation

Supersedes IN_PROGRESS checkpoint above. New gated ADE_Admin_Approval registers
admin_post_ade_positive_preview/review only when existing positive service flag
true, no nopriv hooks. Same flag means previously enabled CLI service now also
allows explicit nonce/capability-protected web flow; shipped undefined/OFF.
One bounded evidence selector + manually entered matching grantID, POST preview
nonce before raw read, separate escaped confirmation of school/old/current/new/
version/declaration notes/references/actor/expiry. Submitted nonce binds candidate,
version/grant/login session; backup/note/APPROVE_ONE_CLAIM required. Apply delegates
to existing atomic service, no edit/bulk/pub/identitypromotion or legacy writes.
Safe fixed inspector redirect; approved UI has no overwrite form. No user config
changes, sourceHTTP or production operation. DefaultGET remains payload-rawread0.

Source_Attestation declaration_for_review reads scoped validated event metadata
without raw reparse (fakeDB tests scope + pair-readcounter). PositiveReview::history
read scoped candidate/school join, keyset20+1, notes4KiBcap/schema/version checks,
escaped reviewer/time/versions/grant/note; history is not currentpermission. Normal
GET nevervalidatesraw automatically. Previewone rawreceiptread, applyone freshread,
exacthistoricalretry raw0. No cross-request authorization cache or globalJSONscan.

Performance fix removes duplicate controller preflight; service/nested preflight,
capability/nonce/flags/locking/raw/version/basehash checks remain. Controller checks
submitted applynonce before calling service (service also checks it). Matched owned
synthetic after-bootstrap querycounts: detailGET109->109, invalidpreviewnonce38->3,
preview203->178, apply159->134, historicalretry70->45. Rawreads/DML: GET0/0, invalid
nonce0/0, preview1/0, apply1/3, retry0/0. Timings noisy; no measured productionlatency
or VPSload improvement claim. Remaining repeated nested schema metadata preflight
is known hotspot; future batch optimization must preserve flags/lease/fencing.

PASS final26offline suites1599checks eachPHP8.2.32/8.4.24 DOM,1531eachwithoutDOM
(HTMLNOTRUN),91PHP lint,84baselinehashes/6originalregressions intact. Existingmanual/
archivecandidate writers, negative-review transaction and R2/R3/R4a intact.
PASS final actualWordPress7.1.4/Directory0.8.9/MySQL8.4.13:151services+89browserchecks,
cleanPHPdiagnostics, corecache unchanged/no wp-config, all25syntheticlegacytables
unchanged. New authenticated realHTTP checkbox-submit covers defaultOFF, exactkeys/
array, GET405, nonce/session/editor/anonymous, wronggrantjobtype, stale version,
withdrawalafterpreview, escapedmetadata/SQL-likenote, confirmation/backup/XSS,
safe redirect, audit/replay/terminalstate, mobile and query/raw/DML counts. History
note matches apostrophe/backslash verbatim. No source-reference browserfetch.

Four ownWordPress/DB/server runs, sequential, removedfinally: initialPASS151+88;
then FAILduring secondadminlogin (30s, no thirdloginPOST or loginerror/PHPdiagnostic);
then PASS151+88 afterharness waits for initialCore200ms autofocus; finaloptimized
PASS151+89. All proofs separately retained: wordpress-before-final-review,
wordpress-attempt-login-timeout, wordpress-before-query-optimization, finalwordpress.
Focusrace hypothesis unproven, not a user-site loginfix; harness now captures only
nonsecret validity booleans/fieldIDs on failure. No autologin bypass or silentretry.
Official fullCLIrunner/userLocalWP/VPSconcurrency/thirdpartyrights/TCPackloss nottested.

Packaging retains only currentQA in ZIP; historicalQA stays inworkspace andGit
history/localbackups, not deleted. Allruntime/tests/vendorfixtures kept; source
and re-extracted bytes checked, extractedoffline rerun. Old7.14ZIP6,614,284bytes,
expanded9,476,668bytes; finalartifact.json records new measuredsizes/reduction.
WordPressUploadReplace needed for oldQA removal; WinSCPmerge mayleaveoldfiles.
Rollback local7.14filebackup, no migration, keep review/event/history/data.
Docs ADMIN_APPROVAL/POSITIVE_REVIEW/readme/acceptance updated. Realfacts0/200, ~55%
foundationestimate remains qualitative. Next durableextractionworker/leasefencing,
then defaultOFF localpublisher+undo, rawretention/quotas and reallicensed sources.
Parent deliveryapprove-dev7.14 at0ac151473dfd8eec741ecb17b60ca72662236189. Latest-only
remote ZIP+guide guardedatomicreplacement after localbundle; main/history preserved.

Dev7.15 ZIP+guide delivered to refs/heads/delivery/admin-review-dev7.15 at 5169f74e398796b698c1c0148c93e3a96e8bdcf4. Atomic create/current-replacement+delete superseded7.14remote, active artifact tree exactly2files. Main unchanged; no historyrewrite, localbundle /workspace/ahda-backups/github-before-dev7.15-delivery.bundle. Finalrelease bytes match151service/89browser WordPress proof and packagedoffline1599/1531 tests. Existingwriters/review/publication defaultsOFF; actualprofile enrichment remains0/200 and estimated foundation~55%.

## dev.7.16 IN_PROGRESS — durable archive batch worker audit/design

Dev7.15 already delivered5169f74e398796b698c1c0148c93e3a96e8bdcf4; latestZIP1,484,741
bytes (-77.6%), expanded3,153,602 (-66.7%). Continuing autonomously into safe local
worker. Do NOT call next worker implemented/tested yet. Design: explicit frozen
subset of pilot NPSN/rawreceiptIDs, CLI-only defaultOFF, no fetch/approval/profile
writes. Per-job+school mutex, lease token/attempt fencing, pending candidate write
and cursor checkpoint in the SAME transaction via narrow internal writer hook;
recovery/retry/cancel preserve committed prefix. Tests must prove lease loss,
insert/checkpoint failure rollback, idempotence, partial progress and legacy hashes.
Existing archive writer cannot be naively wrapped in an outer transaction (nested
START TRANSACTION would implicitly commit); refactor with explicit fenced path,
keep original public record behavior intact and rerun actualWP+offline regressions.

## 2026-11-10 — dev.7.16 DONE: durable fenced local archive worker

Supersedes design IN_PROGRESS. ADE_Archive_Batch newdefaultOFF localCLI module;
explicit strict32KiB input1..200 frozenpilot NPSN/rawreceipt pairs, no duplicate/
newselection. Identity-only stage capturesactualIDs andactor token, no rawreads or
rightsclaim. Enqueuejobsidempotentbyactor+canonicalmanifest; run additionallyneeds
archivecandidateflag. FiveCLI commands batch_stage/enqueue/run/status/control;
no web/cron/network/production/config/legacy writes. Bothflags shippedOFF.

Max3schools/run,20s/96MiB softbudget betweenentries,90slease,3attempts/item. Job
mutex+existing schoolmutex, token/attempt/index/expiry/owner/rawschool fences,
NOWAIT currentjob reads beforecandidatewrites andexpiryCAS atcheckpoint. Refactor
ArchiveCandidates publicrecord into unchangedmanualbody privatewrite with null
fence; narrow record_for_batch adds explicitfence checks andcheckpoint insideSAME
candidate/evidence/link/receipt transaction. No outer START wrapper/nestedcommit
or arbitrarycallback. Replayedreceipt cancheckpoint withoutcandidatechanges.

Prefix/results digest+type/scope/sizevalidated. Failures rollback currententry,
retain committedprefix; max3 thenfailed, explicitretryfailed/cancelled preserveprefix.
Expiredrecover only; liverecover/cancelrefused, ownerenforced, controlappendsimmutable
m2_batch_control jobs audit inside sameTX; auditfailure rollsbackstatus. Fixed3known
semanticVAULTerrors checkpoint outcome=blocked withNULLcandidate_receipt andcode,
continueothers; unknownerrorstoppendingno silentskip. Completed includesblocked,
not allschools enriched; reassessviafreshraw/newexplicitremainingmanifest. Exact
completedmanifestneverreset. No lease/raw/quote/manifest leakedinstatus.

PASS final27offline suites1634checks eachPHP8.2.32/8.4.24 DOM,1566withoutDOM (HTML
NOTRUN),94PHP lint,84baselinehashes/6originalregressionfiles intact. New26fakeDB
batchinput checks freeze200shape only (not200native/facts). Initialtestfloatcase
failed because json_encode(1.0) emittedinteger1; correctedfixture with
JSON_PRESERVE_ZERO_FRACTION, finaltest provesfloatrejection. Not a runtimebugfix.
OfficialCLIparser124checks (WPfacade/fakeDB) includesnewPHPDoc/OFF/dryrun guards.

PASS actualWordPress7.1.4/Directory0.8.9/MySQL8.4.13 final205service+89browser. Initial
188+89 before semanticblocked/controls-audit extension retained separately at
qa/dev7.16/wordpress-before-blocked-audit; finalwordpress authoritative. Bothown
containers/sites/serversremovedfinally, cleanPHPlogs, corecacheunchanged, no
wp-config. OriginalM3web approval/negative review and R2/R3/R4a stilltested.
Four nativeSQLsynthetic schools demonstrate3+1resume; candidatecheckpointfault
rollsbackallcurrentcandidate/evidence/linkrows, committedfirstentryretained;
leaseoldtoken/epoch/expired andfinalCASexpiryblocksideeffects; liveleasecannot
recover, recoverynewtoken,3boundedfailures+retry, cancel+explicitresume; separate
DBsessionjobmutexblockscompetition. Controls auditINSERTfailrollsbackstate, event
appendverified; otherprivilegedactorblocked; corruptedstatshashblocked; wrongraw/
NPSN honestblockedoutcome continuesnextschoolwithoutclaims. All25legacyhashesunchanged.

ActualCOMMIT is executed thenSQLresponseerrorinjected tosimulate lostack. Candidate
receipt+checkpointstaycommitted; failuremarkercan'trewindcompletedjob; exactretry
zero duplicates. This is not genuineTCPdisconnect/processkill testing. LeaseCOMMIT
uncertainty requiresstatus/expiryrecovery; actualOScrashnotE2Etested. No fullofficial
CLIrunner, userLocalWP, real200schools, VPSload, source rights/SEOacceptance tested.

Docs ARCHIVE_BATCH.md/readme/acceptance updated. LatestQA-only packaging kept;
rollbackfiles7.15 withdata/audit retained, no schema change/delete. Realfacts0/200;
~55%foundationestimate remains qualitative, no inflatedpercentage fromtestcounts.
Next localpublisher/undo onsynthetic1school first, broadercontent/rawretention/
quotas, lawfulreal-sourcecollection when networkpolicy permits. No production.
GitHubparent5169f74e398796b698c1c0148c93e3a96e8bdcf4; backup then guardedatomiclatest
ZIP+guide replacement, preservemain/history. Researchbudget18/20first10 unchanged.

Dev7.16 ZIP+guide delivered to refs/heads/delivery/archive-batch-dev7.16 at 770da166e93c8022371251dc152bb2fd6af0ee2c. Atomic create/current-replacement+delete superseded7.15remote, active artifact tree exactly2files. Main unchanged; no historyrewrite, localbundle /workspace/ahda-backups/github-before-dev7.16-delivery.bundle. Finalrelease bytes match205service/89browser WordPress proof and packagedoffline1634/1566 tests. Existingwriters/review/publication defaultsOFF; actualprofile enrichment remains0/200 and estimated foundation~55%.

M4 READ_ONLY audit notes saved docs/PUBLISHER_PREFLIGHT_NOTES.md after7.16 delivery.
Publisher NOT implemented yet. Actual template needs visible citation via existing
profile_source_url; preserve unrelated reference, no cross-schema source_id, require
transactional legacy meta and exact owned undo. Proposed one-school local CLI gate,
no parent/save/badge writes. Further implementation/testing not claimed in7.16.

## dev.7.17 IN_PROGRESS — M4 controlled local publication

Starting implementation from read-only audit, not yet tested/released. CLI-only,
manage_options+review/jobs, defaultOFF plus explicitly configured ONE pilot NPSN.
Publish one approved unchanged claim and conditional visible profile_source_url;
reject unrelated existing citation. No AHDA_Profile::save(), badge/NPSN/name writes.
Runtime InnoDB/schema/unique-key proof; before/after backup rows + audit/receipt in
transaction; exact after-image conflict guard and reverse active publication undo.
Source grant/revocation/raw/basehash fresh for APPLY; undo allowed after revocation
without raw reparse. Synthetic1school tests only under standing tempDB permission.

## 2026-11-10 — dev.7.17 DONE: controlled one-school local publisher + exact undo

Supersedes M4 IN_PROGRESS/audit notes. ADE_Local_Publication CLI-only, defaultOFF
ADE_LOCAL_PUBLISH_ENABLED plus EXACT configured ADE_LOCAL_PUBLISH_NPSN (undefined
bydefault, one pilot school). Requires manage_options+review+jobs/local/CLI/actor/
Directory0.8.9/preflight, backupYES and PUBLISH_LOCAL_CLAIM_WITH_SOURCE. No web
publisher/cron/automatic/bulk/prod operation or config/role/schema migration.
Only approved unchanged programs/curriculum/hours + conditional visible sourceURL.
Existing unrelated citation blocked, sameURI reused unchanged; no AHDA_Profile::save,
NPSN/name/badge/otherfield/source_id crossnamespace mutation. Native template shows
claim and visible #sumber citation. Human declaration is not independent/legalproof.

Read-only publish_stage displays values, fulloldtarget/source state, selectedsafe
sourceURL, declarationrefs/actor/expiry/version/token. ApplyCURRENT-locks school
identity/classification/visibility by NPSN, candidate and positiveaudit/receipt,
grant/revocation/raw/evidence/link/source/legacybasehash; finalexpiry marginchecked
beforeCOMMIT. Candidate staysapproved, publish_statuspublished_local +version/time.
Sourcebodyfromselectedevidence, notclientchosenURL. Pending metadata preimages also
bindtoken, notjustverified-onlybasehash. Existing M2 schoolmutex shared acrosswriters.

Legacytargetrequires InnoDB, exactlyknown7columns, utf8mb4metavalue, unique school/key,
no visibletriggers; completeDBmetadata visibility assumed. Canonicalexactmetakey
rejects CI lookup returninguppercase/paddedkeys the native reader wouldn'tdisplay.
Preserve oldPK/source_id/status/time in bounded backup; oldsourceidnotDiscoveryID.
Exact postwrite readback detects SQLrewrites/truncation/status/IDdrift androllsback.
Legacytarget+citation+candidate+reviewaudit+jobsreceipt commitatomically. Metadata/
images/result/auditchecksums protect backups/changedflags (notDBadmin signatures).

UndoCURRENT-locks sameidentity/candidate/exactownedafterimages; reverseACTIVEapply
order perschool protectssharedcitation. Restoreexistingrows includingoldtime/sourceid/
PK; delete ONLY receipt-provednewlyinsertedrows afterexactimageguard, neveroldprofile.
Exactrestoredreadback beforecommit. Candidate staysapproved, rolled_back_local and
version+1/timeNULL; applyreceipt statusrolled_back butmetadata/result unchanged,
appendseparateundoaudit+receipt. Unchangedcitationuntouched. Otheradmineditconflicts.
Undoallowedwhenrightswithdrawn/sourceblocked/expired andwhenSchoolhidden (doesnot
unhide), stillfrozenidentity/classification. Reapplyfreshpreview/currentgrant only.
Historicalapply/undo replay nevercurrentpermission; result clearlyhistorical_only.

PASS finalactualWordPress7.1.4/Directory0.8.9/MySQL8.4.13:205priornative/services
+69publisher/undo services (=274) +99browser/HTTPHTML checks. Public10checks use
actualDirectorytemplate+native reader+minimaltheme ONLY inownedcopy, fetchasHTML
withredirectsdisabled andparseDOM (notfullfrontendlayout/assets/VPSbenchmark).
Claim/sourcevisibleafterapply, absentafterundo; canonicalone/JSONLDsyntaxretained;
all25originallegacy rowhashesrestored. Badge0/name/NPSNunchanged, sourceID54321
preserved notmappedtoDiscovery7. Nativeexisting-rowrestore andownedinsert/deletetested.

M4 cases: defaultOFF, oneNPSN, manage_options vsreview/jobs, actorboundpreview,
unrelatedsourceconflict, MyISAMpreflightblock/missingunique/latin1/trigger/canonicalkey
rejection, allapply/undoUPDATE/INSERT/COMMITfaults+rowrollback, SQL-layerrewriteexact
readback, pendinglegacyeditstales, wrongprivilegedactor, revoked-beforeapply/blocked
source, two-sessionoldRRcandidate AND Schoolvisibilityreads rejected, hiddenSchool
undo, sharedsource/reverseorder, receiptflagstamper, exactretry. ActualCOMMIT then
injectedresponseerror forapply+undo provesreceiptrecovery; notgenuineTCPdisconnect.

Seven own SQL/site/server runs sequential, allremovedfinally. FirstFAIL was test
expectingPUB_NONTRANSACTIONAL_TARGET whereasexistingpreflight already rejected
MyISAM withLOCAL_OPERATOR_GATE_BLOCKED; testcorrected, no guardweakened. Other6PASS
205+39/48/58/66/69/69publicationchecks and99HTML/browser. Earlierproof separatefolders,
finalqa/dev7.17/wordpress authoritative, cleanPHPlogs/corecache unchanged/no wp-config.
No userLocalWP/fullofficialCLIrunner/VPSload/native200/actualsource/OSkill testclaim.

PASS27offline suites1643checks eachPHP8.2.32/8.4.24DOM,1575withoutDOM (HTMLNOTRUN),
96PHPlint,84baselinehashes/6originaltests unchanged. NewCLI publish_stage/apply/
undo_stage/undo/receipt officialPHPDoc/boolean/disabledguard tests; no fullrunnerE2E.
Existingmanual/archivewriters, M3positive/negative services unchanged inthisrelease.
Only controlledsyntheticlegacywrites occurred; actualuserDB/prod neverconnected.

Expiry/withdrawal NOT auto-erasure ofpublishedcontent; operatorreview/explicitundo/
renewneeded. Already-appliedownbasehash canblockgenericgrantstatus/revalidation;
receiptstatusis history, notongoingrights. OneURI/profile limitation deliberate,
otherexistingreferenceblocked. Rawretention/encryption/totalquota andsource-rights
policy remain gates beforebulkrealcaptures, broadercontentfields/editor/pubUI/
20schoolrollout notdone. Realfacts0/200, not100%MVP/productionready. Parentbaseline
and555460reportedprofiles preserved; no reimport/rebuild/oldprofile deletion.

Networksetup attemptedread only: currentruntimeenforced/customhosts[], draftread
failedtwice "current environment draft could not be verified". No networkconfig
write/persistence/publish claimed, unknownsavedlistnotreplaced. Setupskill requires
reportadditions ratherthanoverwriteunknownlist. docs/NETWORK_RESEARCH_PENDING.md
hasexacttwoalready-consentedGovhosts;20total/2used/18remaining first10scope unchanged.
No Govtrequests or otherexternalSchoolfetch thisturn. Actualsources remainblocked
until cloudsettings action; code-only pipeline cannow be reviewed concretely.

Docs LOCAL_PUBLICATION.md/readme/acceptance/checkpoint. Rollbackfiles7.16 fromlocal
backup preservesjournals/data but7.16cannotM4undo; retain7.17 to retractanyapplyfirst.
Auto_incrementgaps notreset. LatestQA-onlypackaging retained, finalextractedtests/
SHA verified beforeGitHub latestZIP+guide atomicreplacement withlocalbundle.
Parent770da166e93c8022371251dc152bb2fd6af0ee2c; main/history untouched. Next unblock
Govcatalogsettings, lawfulsource/parserfixtures, operatoractual1schoolLocalWPtest,
then20onlyafterexplicitapproval; productionexcluded. Don't repeatcompleted audits.

Dev7.17 ZIP+guide delivered to refs/heads/delivery/local-publisher-dev7.17 at bca0b601f8e63cff08765498040f20eacf297169. Atomic create/current-replacement+delete superseded7.16remote, active artifact tree exactly2files. Main unchanged; no historyrewrite, localbundle /workspace/ahda-backups/github-before-dev7.17-delivery.bundle. Finalrelease bytes match274service/99browser WordPress proof and packagedoffline1643/1575 tests. Existingwriters/review/publication defaultsOFF; actualprofile enrichment remains0/200.


## dev7.18 — DONE: bounded metadata-only raw inventory (2026-11-10 UTC)

Continued after dev7.17, no repeated baseline audit. Network status refreshed,
current restricted/enforced customhosts[]; catalog still excluded, no Gov request,
18 remaining consent unchanged. Unknown network draft not overwritten; required
settings action remains docs/NETWORK_RESEARCH_PENDING.md.

Added ADE_Archive_Vault::inventory and CLI raw_inventory --after --limit --dry-run.
Existing local/manage_jobs/review/actor/schema guard, default25/max100 +lookahead,
prepared id cursor/type query. Metadata only id/status/UTC creation/OCTET_LENGTH:
no raw/summary JSON, school IDs, actor, quotes, URLs returned. No COUNT/OFFSET/
locks/transaction/mutations. Guard/range/errors fail before listing. Canonical
nonnegative ints, ascendingIDs, realdate/plainstatus and sum overflow checked;
future ageNULL/oversized metadata flagged. Lookahead excluded from bytes/cursor.
No quota/retention/encryption/deletion certification or implementation. No snapshot
between pages; page bytes not DB/index/global size. Bound result not engine IO.
No schema/index changed, VPS performance not tested. Do not bulk capture real raw.

PASS 28offline suites1680checks eachPHP8.2/8.4DOM;1612eachwithoutDOM (HTMLNOTRUN),
97PHP lint,84baselinefiles+6originalregressions unchanged. New34inventoryfakechecks,
officialWPCLI synopsis/dispatcher coverage. Initial actor0 test expected wrong
upstreamguard code; corrected test toVAULT_OPERATOR_REQUIRED, no safety weakened.
PASS actualWordPress7.1.4/Directory0.8.9/MySQL8.4 synthetic:212bridge/services
(including7newnative inventory checks),69publisher/undo=281total,99browser/HTML.
Native projection, OCTET_LENGTH totals, next cursor, query no raw/locks, unchanged
Discovery and25legacy hashes confirmed. Ownedcontainer/site/server removed andPHP
logs clean. Same CLI facade/bootstrap/theme limits as7.17, no fullrunner claim.
Existingpublication/review/writers/schema/bootstrap byte-identical to7.17.

Docs RAW_INVENTORY.md, readme, QA diff/logs/security and source-byte manifest.
Rollback files to7.17, no database migration/deletion. Sourcefacts0/200, no actual
userDB orproduction accessed. Next lawfulsource access and actualoneSchooloperator
acceptance, source storage privacy/rights/retention/encryption/quotas beforebulk.
LatestZIP+guide delivery will retain only current pair, preserve main/history and
localbundle; extracted package offline tests and native-tested bytes verified.

Dev7.18 ZIP+guide delivered to refs/heads/delivery/raw-inventory-dev7.18 at f07b71a764184697cb447941009a28a8fcc9752f. Atomic create/current-replacement+delete superseded7.17remote, active artifact tree exactly2files. Main unchanged; no historyrewrite, localbundle /workspace/ahda-backups/github-before-dev7.18-delivery.bundle. Finalrelease bytes match281service/99browser WordPress proof and packagedoffline1680/1612 tests. Existingwriters/review/publication defaultsOFF; actualprofile enrichment remains0/200.

## Operator-selected real example — 20515441 (2026-11-10)

Operator supplied http://ahda.local/sekolah/20515441/smkn-1-bandung/ and
https://smknbandung.sch.id/ after installing7.18, asking real enrichment.
Read-only source inspection confirms existing pilot gate rejects20515441 with
PILOT_NPSN_OUTSIDE_FROZEN_SELECTION. Baseline contract identifies school as SMKN1
BANDUNG KabupatenTulungagung KecamatanBandung, not KotaBandung; current userDB and
website identity not yet checked. Frozen200 Tasikmalaya list remains unchanged.
Do not tell operator pilot extract/publisher will work on this NPSN or bypassgate.
Treat supplied example as separate proposed one-school acceptance scope, not new
national/Tasikmalaya selection. Need bounded host-specific network consent before
fetch (prior consent only two Govcataloghosts), then lawful access/identity check.
No external fetch, local userDB access/write, profile change or code change here.
Existing exact-NPSN `ade sources school --npsn=20515441` is read-only, noHTTP; safe
operator diagnostic for actual legacy identity. Local ahda.local not reachable
from cloud by assumption; never attempt production or infer frontendverified.


## 20515441 source inspection — BLOCKED cloud CONNECT403 (2026-11-10 UTC)

Operator confirmed realLocalWP exactNPSN school196744 SMKN1BANDUNG, Tulungagung/
Bandung/Bantengan,publish. Separately approved website inspection max10HTTPS,
5s/host,oneprocess,noDBwrites/publication. Consent persists; do not ask again.
First request https://smknbandung.sch.id/robots.txt via inheritedproxy/TLSverify,
20stimeout/128KiBcap/no redirects, curl56 CONNECT403 at2026-11-10 11:18:52GMT.
Origin robots/site not retrieved, not proof website itself403/robotsdisallow.
1attempt charged conservatively,9remain. No otherSchoolrequests or claims.
Currentruntime restricted/enforced customhosts[] excludes thisdomain. No live
request_changes tool. Setupdraftread failedcurrentdraftunverified; no configwrite.
Per setupskill do not replaceunknownallowlist; operatoradd smknbandung.sch.id
preservingdomains/presets thenrefreshstatus/freshconnection. PriorGovbudget18
separate. Safealternative operatoropens robots.txt and sharescontent/status; do
not downloadSchoolpages untilrobots/accesspolicy assessed. No newpluginrelease.
20515441 remains outside frozen200; no pilot gate disabled or selectionchanged.
Realcontent/publisherforseparateschool still requires explicit scopedadapter,
sourceidentity/rights and testedpreview; websiteconsent alone notDBwriteapproval.
Evidence docs/qa/smknbandung-20515441/research-status.json +CONNECTheaders.

## Collector 2026.1 — offline milestone DONE, live acceptance PENDING (2026-11-10 UTC)

New operator request: existing AHDA directory + Collector, XLSX school/student2026,
SQLite NPSN key, free templates + optional Ollama, existing-profile integration,
10 LocalWP then100/1000; no production. This expands code scope to national staging,
NOT permission to reimport WordPress, bypass frozen200 Discovery, or run nationalfetch.
Attached Directory0.8.9ZIP byte-matches every baseline entry (SHA in QA integrity).
No existing standalone Collector or national combinedExcel found in availablecheckout;
existing tools are pilotselection/NPSNvalidation and Discovery pipeline. No source
silently replaced. Branch development/collector-2026 created from main8123d8a.

Added collector/ Python CLI: application-id SQLite, explicit XLSX sheet/header mapping,
streamingSHA +read_only rows, mandatorydefusedxml, noformula/privateStudentcolumns,
source SHA/sheet/row/year/optionalURL, strictNPSN (notnamejoin), duplicates provenance,
identity quarantine and numeric/sum/year conflict safeguards. LocalSQLitewrites only.
Per-row atomiccheckpoint/max10000rows/resume; max3attempt/60slease/token+finalfacts
reread+CAS+draft+checkpoint+audit transaction, explicitpause/resume/recover/retry.
Immutable template cache, stale export block, issues cursor. No WordPress/network
calls in import/run. Source-add only pendingURL, no crawling. Optional explicitlocal
Ollama request fixedloopback/nonredirect/context1024/output256/threads2/timeout30s/
32KiB cap; suggestions separate unverified, never replace facts/template. Realmodel
notrun; no APIpaidcalls/credentials. User must installmodel separately ifdesired.

New collector/wordpress-preview.php onlyWPCLI/localahda.local/manage_options/
Directory0.8.9, exactNPSN query and boundedmetadataread, noPosts/INSERT/UPDATE,
identitydifference/hidden blocks, existingdescription PRESERVE_EXISTING; proposed
profile_description diff and beforeSHA. apply_supportedfalse, no approval/publisher
implementation for Collector descriptions. Does not weaken dev7.18threefieldgate.

PASS28unittests (22PythonSQLite +6actualPHPfile using WPfacade), realSQLite fault
rollback/stalelease/currentfacts/export/cache/quarantine/XXE tests. InitialXMLtest
expecteddirectDefusedXmlException butopenpyxlwrapsValueError: fix assertscause
EntitiesForbidden+zeroSchools, no guardweakened; failurelogkept. PHP8.2/8.4lintPASS.
PASSDiscovery28offline suites1680checks PHP8.2DOM,84baselinehash+112Discoveryruntime/
tests/fixtures unchanged versus7.18ZIP. SourceDirectoryZIPallentriesmatch baseline.
PASSsyntheticSQLite10/100/1000 uniqueSchools/drafts, no duplicatecache onrerun.
1000Linux: import2.025s/generate3.825s/processpeakRSS39903232bytes, notWindows/VPS/
LocalWP/555kbenchmark. Temporary test DB/workbooks removed. Existingoperatorpilot
workbook200imported totemporarySQLite,10identitydrafts,0studentcountclaims (no data),
originalSHAunchanged. No publication or factualsourceverification claimed.

NOTTESTED/PENDING: combinednationalExcel2026 unavailable; existingCollector source
elsewhere unknown; actualWindows4GB/modelOllama/10NPSNLocalWPfrontend nottested.
No realuserDB/productionwrite or realwebsitefetch thismilestone. Earlierwebsite
consent/budgets persist separately, cloudnetworkblocked unchanged. Realpublished
factual enrichment remains0/200pilot. Search/HTTPcache/crawl and descriptionadmin
approval/apply/undo notimplemented. See docs/COLLECTOR_AUDIT_2026.md and collector/
README.md Windowscommands, limits, safe preview. Do not claim entire sixstagesdone.

Next obtain actualcombinedExcel + anyseparateCollector source; auditheaders/count
semantics and import10NPSNstaged; operatorLocalWPpreview10; sourcesrights/network;
implementdescriptionpublisher withnonce/capability/backup/hashconflict/transaction/
audit/undo then oneapprovedSchooltest before10/100/1000. RollbackCollectorfiles+
stoppedSQLitebackup; no WordPressschema/data migration or oldprofiledeletion.

Collector source/docs/tests delivered to refs/heads/development/collector-2026 at 4fafb4ae626402b10bd981f409fe93e4beb8ce53. Main and plugin7.18delivery unchanged. Source-only new branch, no dataset/SQLite/Excel upload. NativeuserLocalWP/combinedExcel/Ollamaactual remain pending.


## Collector2026.2 — DONE priority and header tool; national workbook TRANSFER_BLOCKED

Operator uploaded AHDA_Gabungan_Sekolah_Peserta_Didik_2026.xlsx and requested
SMP/MTs first, then SMA/SMK/MA/equivalent. download_file failed "file exceeds the
executor transfer limit of32MiB". File content/header/hash/counts unavailable;
DO NOT claim national import/audit PASS or substitute oldpilotresults. Required
next: operator local inspect-xlsx headerJSON or filtered SMP/MTs workbook parts
<32MiB without personalstudentdata. OriginalExcel preserved. No alternateupload
or transfer attempted, no need repeat permission for offline stagedimport.

Implemented explicit school_form priority0 SMP/MTs+listed equivalents,1 upper
secondary,2unknown/other. No name inference, default excludes2, --include-other
explicit optin. Mapping example adds school_form placeholder to match actualheader.
SQLite schema2 jobs.priority+ready partialindex, EXPLAIN confirms indexedorder/no
TEMPsort. Explicit upgrade only, v1 backup exclusive/activeleaseguard/transactional
ALTER+classify+index+version+audit, preservescachedrafts/status/facts. Rollbackold
source requires stoppedDB schema1backup; no WordPressschema/data changes.

New inspect-xlsx reads firstrowassumedheader via boundeddefusedXML ZIP streams,
sharedstringsonlyneededindices/no fulltable allocation. Caps metadata1MiB,100sheets,
256cols,16MiBworksheetheader scan,64MiBsharedstring scan; no worksheetrowcountinferred.
No DBcreated forinspect (--dbunused), no studentdatarows returned. User must verify
firstrowisheader before sharingmetadata. Importerfullread_only/sharedstringcap stays.

PASS38UNIQUE tests (22previousPython,10newpriority/migration/header,6PHPfacade).
Initial58PASS accidentallyrediscovered importedoldTestCase; fixedfixtureimport,
retainedinitiallog and do not inflatecount. Faultmigrationrollsback, backupidempotent,
activeleaseblocked, stalecontrols/regressions, readyindex plan, mixedNPSNordering,
unknownformhold, inline/richsharedstrings/privateRows and XXE rejection tested.
Synthetic1000 mixedlower/upper SQLite PASS;40MBLinuxRSS approx, notWindows555k.
Oldpilotworkbook (NOTnewnationalfile):177priority0 precede23priority1,200identity
SQLite drafts, originalhashunchanged, ownDBremoved; no studentsclaims/publishing.
PluginDirectory/Discovery/helper bytesunchanged, no websitefetch/userWPDB/prodaccess.

Docs COLLECTOR_PRIORITY_2026.md/README upgrade+Windowsheaderinstructions, QA
collector-priority-2026 logs/bench/order/integrity. Next inspectrealheaders, import
actualSMPMTs subset10, operatorLocalWPpreview, lawfulsources and descriptionapproval/
publisher separate. Branch development/collector-2026 continues parent4fafb4ae.
Do not rebuild/replace frozen200 Tasikmalaya or claim allnationalprofiles enriched.
