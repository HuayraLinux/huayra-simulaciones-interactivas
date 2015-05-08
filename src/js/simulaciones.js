var exec = require('child_process').exec;
var sim_path = "/usr/share/huayra-simulaciones-interactivas/data/simulaciones/";
var scr_path = "file:///usr/share/huayra-simulaciones-interactivas/data/screenshots"
var java_jar = "java -jar ";

function load_simus(content){
    content.html('');

    for(obj in categories){
        categories[obj]['simus'] = categories[obj]['simus'].map(function(k){ if( typeof(k) == "string" ) {s = simulations[k]; s.name = k; return s;} });
        categories[obj]['scr_path'] = scr_path;
        categories[obj]['cant'] = categories[obj]['simus'].length;
        content.append(
            Mustache.render($('#tmpl-category').html(), categories[obj])
        );
    }
}

function fn_open_simulation(){
    open_simulation($(this));
}

function open_simulation(sim_slide){
    var sim_name = sim_slide.attr('class').match(/sim-(.*)/gi);
    $('.'+sim_name).off('click').css('cursor','wait');

    exec(java_jar + sim_path + sim_slide.data('open') , function(error, stdout, stderr) {
        console.log('stdout: ' + stdout);
        console.log('stderr: ' + stderr);
        if (error !== null) {
            console.log('exec error: ' + error);
        }

        $('.'+sim_name).on('click', fn_open_simulation).css('cursor','pointer');
    });

}

function fn_filter_sim(){
    filter_sim($('#filter-sim'));
}

function filter_sim(input){
    console.log("//*//*[contains(title, '_STR_')]".replace('_STR_',
                                                           input.val()));

    var s_res = JSON.search(simulations,
                            "//*//*[contains(title, '_STR_')]//file".replace('_STR_',
                                                                             input.val()));
    //categories["filtrar"]['simus'] = s_res.map(function(s){ return s.replace('_es.jar', ''); });
    categories.filtrar.simus = s_res.map(function(s){ return s.replace('_es.jar', ''); });
    load_simus($('#content'));
    setTimeout(function(){ Reveal.slide(7); },1000);
}

$(document).ready(function(){
    load_simus($('#content'));

    $('.simudescription').on('click', fn_open_simulation);

    $('#btn-filter-sim').on('click', fn_filter_sim);
    //$('#filter-sim').on('keyup', fn_filter_sim);

    Reveal.initialize({
        controls: true,
        progress: true,
        history: true,
        center: true,
        transition: 'slide'
    });
});
