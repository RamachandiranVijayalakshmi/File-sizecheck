# File-size check.
1. **check file is empty or not**
2. **import os**
3. **file-path pass the  parameter values**

## Sample code check file empty or not

```sh
if os.stat(a).st_size == 0:
        print('File is empty')
    else:
        print('File is not empty')
```
## Example output
```sh
The file is not empty
```
            
        
