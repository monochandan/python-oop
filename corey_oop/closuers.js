function html_tag(tag){
    function wrap_text(msg){
        console.log('<'+ tag + '>' + msg + '</' + tag + '>');
    }
    return wrap_text
}

print_h1 = html_tag('h1')

print_h1('My HeadLine!')
print_h1('Content')