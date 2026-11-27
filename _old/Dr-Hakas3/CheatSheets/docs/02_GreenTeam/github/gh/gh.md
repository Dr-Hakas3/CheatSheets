---
title: gh
parent: github
grand_parent: Green Team
nav_order: 1
---
# gh

---

## Summary

github CLI

---

## Delete Deploy log

1. auth login
2. script execute
3. check

### script

```zsh
for id in $(gh api repos/<USERNAME>/<RepoName>/deployments --jq '.[].id'); do
  echo "Processing deployment $id"

  gh api \
    repos/<USERNAME>/<RepoName>/deployments/$id/statuses \
    -f state=inactive

  gh api \
    -X DELETE \
    repos/<USERNAME>/<RepoName>/deployments/$id
done
```


### check command

```zsh
gh api repos/Dr-Hakas3/CheatSheets/deployments
```