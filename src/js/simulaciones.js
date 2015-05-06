var exec = require('child_process').exec;
var sim_path = "/usr/share/huayra-simulaciones-interactivas/data/simulaciones/";
var java_jar = "java -jar ";

function load_simus(content){
    content.html('');

    for(obj in categories){
        categories[obj]['simus'] = categories[obj]['simus'].map(function(k){ return simulations[k]; });
        categories[obj]['cant'] = categories[obj]['simus'].length;
        content.append(
            Mustache.render($('#tmpl-category').html(), categories[obj])
        );
    }
}


function open_simulation(sim_jar){

    console.log( java_jar + sim_path + sim_jar );

    exec(java_jar + sim_path + sim_jar , function(error, stdout, stderr) {
        console.log('stdout: ' + stdout);
        console.log('stderr: ' + stderr);
        if (error !== null) {
            console.log('exec error: ' + error);
        }
    });

}


$(document).ready(function(){
    load_simus($('#content'));

    $('.simudescription').on('click', function(){
      open_simulation($(this).data('open'));
    });

    Reveal.initialize({
        controls: true,
        progress: true,
        history: true,
        center: true,
        transition: 'slide'
    });
});
