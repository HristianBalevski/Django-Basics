from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape, mark_safe, escape
import mistune

register = template.Library()


@register.filter
def lower(value):
    return value.lower()


"""
Lines 6 to 7 define the function implementing the filter. The filtered value is the first argument to the function.
This implementation assumes the value is a string. The string’s .lower() method gets called and the result returned. 
What you return from your filter function gets rendered in the template.
The Library object provides methods for registering tags and filters. 
You may call these methods directly, but the better way is to use them as decorators. 
Decorating the function makes it clear to other programmers that it’s registered as a tag or filter.
"""


@register.filter
def first_letters(iterable):
    result = ""
    for item in iterable:
        result += item[0]

    return result


"""
Recall from dinofacts/views.py that the dinosaurs value is a list containing "Tyrannosaurus", "Stegosaurus", "Raptor",
and "Triceratops". The result above is the first letter of each of these mighty reptiles: "TSRT".
"""


@register.filter(name="nth_letters", is_safe=True)
def other_letters(iterable, num):
    result = ""
    for item in iterable:
        if len(item) <= num or not item[num - 1].isalpha():
            result += " "
        else:
            result += item[num - 1]

    return result


"""
Line 36 adds the name argument to the @register.filter() decorator. 
This makes the filter’s name in the template different from the implementing function.
Here, the filter gets named nth_letters even though the function that implements it is other_letters().
Note that is_safe=True indicates to Django that the output of this filter doesn’t contain characters that will break HTML.

Line 37 defines the function. The value to filter is the first argument, and the filter’s parameter is the second.

Lines 39 to 43 iterate over the value and build the resulting string.
Line 40 is a safety check. If you’re looking for the tenth index in an eight-letter string, it’ll use a space (" ") instead. 
Also, if the n-th character isn’t a letter, you use a space to avoid accidentally returning characters that break HTML.

In the example above, the is_safe=True argument to the registration decorator tells Django that this filter promises not to output any troublesome characters. 
A safe string passed to a filter does not get escaped by Django. The default value for is_safe is False.

Note that is_safe=True is not marking your filter result as safe. That’s a separate step for which you are responsible. 
The call to .isalpha() above ensures that all output from this function is safe, so there’s no need for an extra step.

Be careful when determining whether your filter is safe or not, especially when removing characters. 
A filter that removed all semicolons would break HTML entities that depend on semicolons, like &amp;.
"""


@register.filter(needs_autoescape=True)
@stringfilter
def letter_count(value, letter, autoescape=True):
    if autoescape:
        value = conditional_escape(value)

    result = (
        f"<i>{value}</i> has <b>{value.count(letter)}</b> "
        f"instance(s) of the letter <b>{letter}</b>"
    )

    return mark_safe(result)


"""
The @stringfilter decorator on line 74 indicates that this filter only takes strings. 
Django turns the filter’s value into a string before passing it into the filter.

Line 73 uses the needs_autoescape parameter in the registration decorator. 
This tells Django to add another argument to the filter function: autoescape. 
The value of this argument will indicate whether autoescaping is on or off for the scope of this filter.

Line 75 declares the filter function and includes the autoescape argument mentioned above. 
This argument should default to True so that you’re in autoescape mode if your code calls the function directly.

Lines 76 to 77 replace value with the result of conditional_escape() if autoescape is True. 
The conditional_escape() function escapes the string but is smart enough to not escape something that has already been escaped.

Lines 79 to 82 build the returning string. 
Because the letter_count filter outputs HTML with bold and italic tags, it has to be autoescape-aware. 
The f-string on line 80 uses the contents of value, which got appropriately escaped in lines 76 to 77, as needed. 
The result string contains value in italics and the letter count in bold.

Line 84 calls mark_safe() on the result variable. 
Because the filter is outputting HTML that should be displayed, the function must mark the string as safe. 
This tells Django not to further escape the contents so the bold and italic tags get rendered by your browser.

The @stringfilter decorator is a quick shortcut that ensures your filter will only have to deal with strings. 
The needs_autoescape argument and its corresponding autoescape argument give you fine-grained control over what the filter does and doesn’t autoescape.
"""


@register.filter(expects_localtime=True)
def bold_time(when):
    return mark_safe(f"<b>{when}</b>")


@register.simple_tag
def mute(*args):
    return ""


@register.simple_tag
def make_ul(iterable):
    content = ["<ul>"]
    for item in iterable:
        content.append(f"<li>{escape(item)}</li>")

    content.append("</ul>")
    content = "".join(content)
    return mark_safe(content)


@register.simple_tag(takes_context=True)
def dino_list(context, title):
    output = [f"<h2>{title}</h2><ul>"]
    for dino in context["dinosaurs"]:
        output.append(f"<li>{escape(dino)}</li>")

    output.append("</ul>")
    output = "".join(output)

    context["weight"] = "20 tons"
    return mark_safe(output)


@register.inclusion_tag("sublist.html")
def include_list(iterator):
    return {"iterator": iterator}


"""
If you’re writing a tag that uses a lot of HTML, using @inclusion_tag is a better way to keep the HTML separate from the code.
"""


@register.tag(name="markdown")
def do_markdown(parser, token):
    nodelist = parser.parse(("endmarkdown",))
    parser.delete_first_token()
    return MarkdownNode(nodelist)


class MarkdownNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        content = self.nodelist.render(context)
        result = mistune.markdown(str(content))
        return result


@register.tag()
def shownodes(parser, token):
    nodelist = parser.parse(("endshownodes",))
    parser.delete_first_token()
    return ShowNodesNode(token, nodelist)


class ShowNodesNode(template.Node):
    def __init__(self, token, nodelist):
        self.token = token
        self.nodelist = nodelist

    def render(self, context):
        result = [
            "<ul><li>Token info:</li><ul>",
        ]

        for part in self.token.split_contents():
            content = escape(str(part))
            result.append(f"<li>{content}</li>")

        result.append("</ul><li>Block contents:</li><ul>")
        for node in self.nodelist:
            content = escape(str(node))
            result.append(f"<li>{content}</li>")

        result.append("</ul>")
        return "".join(result)
