#! /usr/bin/env nu

const RFC3339_FORMAT = "%Y-%m-%dT%H:%M:%S%z"

source ./sync.nu


let sync_data = get-sync-data
let completed_tasks = get-completed-tasks
let completed_tasks_stats = get-stats


let endpoints = {
    "sync": $sync_data,
    "completed/get_all": $completed_tasks,
    "completed/get_stats": $completed_tasks_stats
}

let metadata = {
   "created_at": (date now | format date $RFC3339_FORMAT),
}

let result =  {endpoints: $endpoints, metadata: $metadata}


$result | save -f todoist-export.json