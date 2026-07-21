# QiLife People & Events

Notes: Merged people/contact model and events/calendar-visible model.
QiCode: § 04.02.007
Sort Key: 04.02.007
Status: active
Tags: Core, Hubs
Type: Record Type
Version: Reconciled V1

**Merged from:** QiLife Data Model Spine  

**System:** QiOS  

**Parent App:** QiLife  

**Status:** Active Doctrine  

**Version:** Reconciled V1

## People

People is a broad entity/contact model.

It is not CRM.

```
people
├── id
├── display_name
├── legal_name
├── type
├── relationship
├── role
├── email
├── phone
├── address
├── notes
├── tags_json
├── metadata_json
├── created_at
├── updated_at
├── archived_at
└── deleted_at
```

## People Types

```
person
family
friend
vendor
government
organization
agency
care_provider
legal_contact
financial_contact
service_provider
neighbor
unknown
```

## People Rule

Do not create separate tables for vendors, agencies, government contacts, care team, and organizations.

Use one table with `type`, `relationship`, `role`, tags, and metadata.

## Events

Events are scheduled or historical calendar-visible items.

```
events
├── id
├── title
├── description
├── start_time
├── end_time
├── location
├── bucket_key
├── thread_id
├── status
├── source_qibit_id
├── external_calendar_id
├── external_event_id
├── created_at
├── updated_at
├── archived_at
└── deleted_at
```

## Event Statuses

```
scheduled
completed
cancelled
missed
archived
```

## Event Rule

Events may sync with Google Calendar later through QiConnect.

QiLife should not assume Google Calendar is the only calendar source.