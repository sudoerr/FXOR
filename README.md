# FXOR (File XOR)
XOR files and safely save them in server storage.
Interacting with **Malicious** file may cause many problems in your server/system.
The FXOR can help you `write` and `read` files byte by byte changing data
with XOR operator and provided as a IO Base class.

## Know More About FXOR
To use fxor you need to understand basic of it. first of all you need some arguments :
> 1. An integer key in range(0, 256)
> 2. Path to a file
> 3. File open mode `w` for write mode or `r` read mode
> 4. Fast mode for `True` or `False` which effects writing speed and memory usage
> 5. File real name or even None

Now let's see what does each one of these arguments do:
- key is used for XOR operation and you need same key for reading a file XORed with that key.
- Path to a file or XORed file in read mode
- Open mode
- Fast mode which can use more RAM if you set it to `True`
- File name if you need to use.

<br>

---

<br>

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
Here is the arguments we passed :
1. File name to open
2. File name to write to
3. The key
4. File open mode

#### Feel free to contribute...
