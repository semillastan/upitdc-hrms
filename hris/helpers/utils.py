
def replace_urlpattern(urlpatterns, replacement):
    found = False
    index = 0
    
    if hasattr(replacement, 'name') and replacement.name:
        name = replacement.name
        regex = None
    else:
        name = None
        regex = replacement.regex.pattern
    
    while not found and index < len(urlpatterns):
        pattern = urlpatterns[index]
        if hasattr(pattern, 'url_patterns'):
            found = replace_urlpattern(pattern.url_patterns, replacement)
        else:
            if name and hasattr(pattern, 'name'):
                if pattern.name == name:
                    del urlpatterns[index]
                    urlpatterns.append(replacement)
                    found = True
            elif pattern.regex.pattern == regex:
                del urlpatterns[index]
                urlpatterns.append(replacement)
                found = True

        if not found:
            index += 1
    
    return found
    
    
