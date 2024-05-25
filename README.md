# FXOR (File XOR)
XOR files and safely save them in server storage.
Interacting with **Malicious** file may cause many problems in your server/system.
The FXOR can help you `write` and `read` files byte by byte changing data
with XOR operator and provided as a IO Base class.


## Usage :
### Import into your project :
```python
from fxor import FileXOR

chunk_size = 1024 * 1024 # 1 MB

# Write/Create new file
with FileXOR(8, "path/to/output_file", "w", True, "output_file") as f:
    with open("path/to/input_file", "rb") as f2:
        while True:
            data = f2.read(chunk_size)
            f.update_write(data)
            if len(data) < chunk_size:
                break

# Read from XORed file
with FileXOR(8, "path/to/input_file", "r", True, "input_file") as f:
    with open("path/to/output_file", "wb") as f2:
        while True:
            data = f.read(chunk_size)
            f2.write(data)
            if len(data) < chunk_size:
                break
```
### Use Command Line Interface

```shell
python3 fxor.py "1.jpg" "2.enc" 8 "w"
```
```shell
python3 fxor.py "2.enc" "2.jpg" 8 "r"
```


