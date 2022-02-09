# cprint
Python function to print a list of items in a columnar format for easy reading.

## Example Usage

```
>>> items = dir(str)
>>> cprint(items)
__add__             __mod__            find           maketrans   
__class__           __mul__            format         partition   
__contains__        __ne__             format_map     removeprefix
__delattr__         __new__            index          removesuffix
__dir__             __reduce__         isalnum        replace     
__doc__             __reduce_ex__      isalpha        rfind       
__eq__              __repr__           isascii        rindex      
__format__          __rmod__           isdecimal      rjust       
__ge__              __rmul__           isdigit        rpartition  
__getattribute__    __setattr__        isidentifier   rsplit      
__getitem__         __sizeof__         islower        rstrip      
__getnewargs__      __str__            isnumeric      split       
__gt__              __subclasshook__   isprintable    splitlines  
__hash__            capitalize         isspace        startswith  
__init__            casefold           istitle        strip       
__init_subclass__   center             isupper        swapcase    
__iter__            count              join           title       
__le__              encode             ljust          translate   
__len__             endswith           lower          upper       
__lt__              expandtabs         lstrip         zfill       
```
`format_spec` follows the [Python String Format Mini-Language](https://docs.python.org/3/library/string.html#format-specification-mini-language), 
with the exception that the character `w` stands in for the `width` specifier.

In this case, `format_spec` is set to align the columns right:
```
>>> cprint(items, columns=3, format_spec='{:>w}')
          __add__           __rmod__        istitle
        __class__           __rmul__        isupper
     __contains__        __setattr__           join
      __delattr__         __sizeof__          ljust
          __dir__            __str__          lower
          __doc__   __subclasshook__         lstrip
           __eq__         capitalize      maketrans
       __format__           casefold      partition
           __ge__             center   removeprefix
 __getattribute__              count   removesuffix
      __getitem__             encode        replace
   __getnewargs__           endswith          rfind
           __gt__         expandtabs         rindex
         __hash__               find          rjust
         __init__             format     rpartition
__init_subclass__         format_map         rsplit
         __iter__              index         rstrip
           __le__            isalnum          split
          __len__            isalpha     splitlines
           __lt__            isascii     startswith
          __mod__          isdecimal          strip
          __mul__            isdigit       swapcase
           __ne__       isidentifier          title
          __new__            islower      translate
       __reduce__          isnumeric          upper
    __reduce_ex__        isprintable          zfill
         __repr__            isspace
```
