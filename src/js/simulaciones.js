
function load_simus(content){
    content.html('');

    for(obj in categories){
        categories[obj]['simus'] = categories[obj]['simus'].map(function(k){ return simulations[k]; });
        content.append(
            Mustache.render($('#tmpl-category').html(), categories[obj])
        );
    }
}
