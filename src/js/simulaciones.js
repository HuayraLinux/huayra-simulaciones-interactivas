var exec = require('child_process').exec;
var sim_path = "/usr/share/huayra-simulaciones-interactivas/data/simulaciones/";
var scr_path = "file:///usr/share/huayra-simulaciones-interactivas/data/screenshots"
var java_jar = "java -jar ";

function load_simus(content){
    content.html('');

    for(obj in categories){
        categories[obj]['simus'] = categories[obj]['simus'].map(function(k){ return simulations[k]; });
        categories[obj]['scr_path'] = scr_path;
        categories[obj]['cant'] = categories[obj]['simus'].length;
        content.append(
            Mustache.render($('#tmpl-category').html(), categories[obj])
        );
    }
}


function open_simulation(sim_slide){

    sim_slide.css('cursor','wait');

    exec(java_jar + sim_path + sim_slide.data('open') , function(error, stdout, stderr) {
        console.log('stdout: ' + stdout);
        console.log('stderr: ' + stderr);
        if (error !== null) {
            console.log('exec error: ' + error);
        }


        sim_slide.css('cursor','pointer');
    });

}


function filter_sim(input){
    Reveal.setState(7);
    console.log( input.val() );

    console.log("//*//*[contains(title, '_STR_')]".replace('_STR_',
                                                           input.val()));

    var s_res = JSON.search(simulations,
                            "//*//*[contains(title, '_STR_')]//file".replace('_STR_',
                                                                             input.val()));
    categories["filtrar"]['simus'] = s_res.map(function(s){ return s.replace('_es.jar', ''); });
    load_simus($('#content'));
}

$(document).ready(function(){
    load_simus($('#content'));

    $('.simudescription').on('click', function(){
      open_simulation($(this));
    });

    $('#btn-filter-sim').on('click', function(){
      filter_sim($('#filter-sim'));
    });
    $('#filter-sim').on('keyup', function(){
      filter_sim($(this));
    });

    Reveal.initialize({
        controls: true,
        progress: true,
        history: true,
        center: true,
        transition: 'slide'
    });
});
