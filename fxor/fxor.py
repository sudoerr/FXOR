
import io
import os


class FileXOR(io.IOBase):
    def __init__(self, key:int, file:str, mode:str="w", fast_mode:bool=False, name="unknown"):
        """
        Quarantine file with simple XOR on write and read
        :param key: XOR value between 0-256, must be same always
        :param file: file source or destination
        :param mode: w or r (write or read)
        :param fast_mode: if True will cause high memory usage but faster xor operation on write mode
        """
        self.__key = key
        self.__fast_mode = fast_mode
        self.__name = name
        self.__file_path = file
        self.__mode = mode
        if mode == "w":
            self.__file = open(file, "wb")
        elif mode == "r":
            self.__file = open(file, "rb")
        else:
            raise Exception("mode can only be w or r")


    @property
    def name(self):
        return self.__name
    @property
    def mode(self):
        return self.__mode
    @property
    def key(self):
        return self.__key
    @property
    def fast_mode(self):
        return self.__fast_mode
    @property
    def file_path(self):
        return self.__file_path


    def update_write(self, data:bytes):
        # check for mode
        if self.__mode != "w":
            raise Exception(f"Error when trying to write to file with mode \"{self.__mode}\"")
        # check for fast mode
        if self.__fast_mode:
            # read each byte, XOR with key and append to bytes list
            data = bytes([byte ^ self.__key for byte in data])
            self.__file.write(data)
        else:
            for c in data:
                self.__file.write((c ^ self.__key).to_bytes(1, "big"))

    def update_read(self, chunk:int):
        # read each byte, XOR with key and append to bytes list
        data = bytes([byte ^ self.__key for byte in self.__file.read(chunk)])
        return data

    def read(self, _n=None):
        if _n == None:
            _n = os.path.getsize(self.__file_path)
        return self.update_read(_n)

    # to use "with" statement in FileXOR invocations
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__file.close()

    def close(self):
        self.__file.close()



if __name__ == "__main__":
    import sys
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    key = int(sys.argv[3])
    mode = sys.argv[4]
    chunk_size = 1024*1024

    if mode == "w":
        with FileXOR(key, output_file, mode, True, "input_file") as f:
            with open(input_file, "rb") as f2:
                while True:
                    data = f2.read(chunk_size)
                    f.update_write(data)
                    if len(data) < chunk_size:
                        break

    elif mode == "r":
        with FileXOR(key, input_file, mode, True, "input_file") as f:
            with open(output_file, "wb") as f2:
                while True:
                    data = f.read(chunk_size)
                    f2.write(data)
                    if len(data) < chunk_size:
                        break



