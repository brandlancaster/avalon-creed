#!/bin/bash
# usage: upload.sh <file-with-jwt>   (Avalon Creed asset upload via curl)
JWT=$(rg -o 'eyJ[A-Za-z0-9_.-]+' "$1" | head -1); A=https://api.cloudflare.com/client/v4/pages/assets
curl -s -m 120 -X POST $A/upload -H "Authorization: Bearer $JWT" -H 'Content-Type: application/json' --data @/tmp/creed_upload.json | python3 -c "import json,sys;r=json.load(sys.stdin);print('upload',r['success'],r['result'])"
curl -s -m 30 -X POST $A/upsert-hashes -H "Authorization: Bearer $JWT" -H 'Content-Type: application/json' --data @/tmp/creed_hashes.json; echo
curl -s -m 30 -X POST $A/check-missing -H "Authorization: Bearer $JWT" -H 'Content-Type: application/json' --data @/tmp/creed_hashes.json; echo
