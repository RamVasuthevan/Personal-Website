#! /usr/bin/env nu

use std log

const COMPLETED_TASKS_MAX_LIMIT = 200
const ARCHIVED_SECTIONS_MAX_LIMIT = 100

def get-sync-data [] {
    log info "Getting sync data"
    let result = http post --headers [ "Authorization" $"Bearer ($env.TODOIST_API_TOKEN)" ] --content-type "application/x-www-form-urlencoded" https://api.todoist.com/sync/v9/sync { sync_token: "*", resource_types: '["all"]' }
    $result
}

def get-completed-tasks-with-offset [offset: int] {
    log info $"Getting completed tasks with offset: ($offset)"
    const annotate_notes = true
    const annotate_items = true
    const limit = $COMPLETED_TASKS_MAX_LIMIT
    let url = $"https://api.todoist.com/sync/v9/completed/get_all?limit=($limit)&annotate_notes=($annotate_notes)&annotate_items=($annotate_items)&offset=($offset)"

    let result = http post --headers [ "Authorization" $"Bearer ($env.TODOIST_API_TOKEN)" ] --content-type "application/x-www-form-urlencoded" $url { sync_token: "*", resource_types: '["all"]' }
    
    $result
}

def get-completed-tasks [] {
    mut results = []
    mut offset = 0

    while true {
        let result = get-completed-tasks-with-offset $offset
        $results = $results | append $result
        $offset += $COMPLETED_TASKS_MAX_LIMIT

        if ($result | get items | is-empty) {
            break
        }
    }

    $results
}

def get-stats [] {
    log info "Getting stats"
    let result = http get --headers [ "Authorization" $"Bearer ($env.TODOIST_API_TOKEN)" ] https://api.todoist.com/sync/v9/completed/get_stats
    $result
}
