from zope import interface

class IPyContainerValueIterator(interface.Interface):
    """Find Container values based on a key"""
    def values(config, key):
        """Iterator of values in a container matching given key
        
        This acts based on the top level container type.  For mappings, this 
        will search keys and return the corresponding value.
        
        For others (list, set, tuple), this will iterate the container and 
        search for mapping entries.  Each mapping found will be processed as 
        above.
        
        Note:
            This is not a recursive method, it will only search 1 level deep
            on non-mappings  
        
        Args:
            config: A Python container type (Dict, List, Set, Tuple).
            key: Hashable key to match on
        Returns: Iterator of objects matched as values for given key
        """

class IPyContainerValue(interface.Interface):
    """Find container values based on a key"""
    def get(*args, **kwargs):
        """Get the first container value matching key
        
        See IPyContainerValueIterator for information on how search for key
        is performed.
        
        Raises: KeyError if key is not found and default is not given
        
        Args:
            Ordered keys to search in config.  To find 'value1' in this
            container {'key1': {'key2': 'value1'}}, you would make a call
            to get('key1', 'key2')
        Kwargs:
            default: value to return if given args are not a valid mapping.
            
        Returns: object value from key or default
        """
    def query(*args):
        """Get the first container value matching key, if available
        
        See IPyContainerValueIterator for information on how search for key
        is performed.
        
        Args:
            [see get()]
            
        Returns: object value from key or None if key is not found
        """