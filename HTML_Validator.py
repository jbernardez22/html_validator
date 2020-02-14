#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    list_of_tags = _extract_tags(html)
    stack = []
    for i in list_of_tags:
        if (list_of_tags[i][1] != "/"):
            stack.append(list_of_tags[i])
        else:
            top = stack.pop()
            if(top[1:-2] != list_of_tags[2:-2]):
                return False
    if(stack != []):
        return False 
    return True

        # if opening add to stack
        #if not an opening, pop top of the stack, compare string in opening to string in closing tag
        # if the same, pop off the top
        # if not the same, return false
        #outside the for loop return false 
        

    # HINT:
    # use the _extract_tags function below to generate a list of html tags without any extra text;
    # then process these html tags using the balanced parentheses algorithm from the book
    # the main difference between your code and the book's code will be that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    list_of_tags = []
    new_string = ""
    for i in range(len(html)):
        if(html[i]=="<"):
            counter = 0 
          #  new_string =  "<"
            while(html[i+counter]!=">"):
           # if(html[i+1]!= ">"):
                new_string = new_string + html[i+counter]
                counter +=1 
            new_string = new_string + ">"
            list_of_tags.append(new_string)
            new_string = ""
    return list_of_tags
                           


