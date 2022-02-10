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
>>> cprint(items, columns=6, format_spec='{:>w}')
         __add__            __init__           __rmul__     format_map           join       rstrip
       __class__   __init_subclass__        __setattr__          index          ljust        split
    __contains__            __iter__         __sizeof__        isalnum          lower   splitlines
     __delattr__              __le__            __str__        isalpha         lstrip   startswith
         __dir__             __len__   __subclasshook__        isascii      maketrans        strip
         __doc__              __lt__         capitalize      isdecimal      partition     swapcase
          __eq__             __mod__           casefold        isdigit   removeprefix        title
      __format__             __mul__             center   isidentifier   removesuffix    translate
          __ge__              __ne__              count        islower        replace        upper
__getattribute__             __new__             encode      isnumeric          rfind        zfill
     __getitem__          __reduce__           endswith    isprintable         rindex
  __getnewargs__       __reduce_ex__         expandtabs        isspace          rjust
          __gt__            __repr__               find        istitle     rpartition
        __hash__            __rmod__             format        isupper         rsplit
```
