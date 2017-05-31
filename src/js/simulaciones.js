var exec = require('child_process').exec;
var sim_path = "/usr/share/huayra-simulaciones-interactivas-data/simulaciones/";
var java_jar = "java -jar ";

var categories = require('/usr/share/huayra-simulaciones-interactivas-data/categories');
var simulations = require('/usr/share/huayra-simulaciones-interactivas-data/simulations');

process.mainModule.exports.init(require('nwjs-hack').set_wmclass.bind(null, "huayra-simulaciones-interactivas", true));


function load_simus(content){
    content.html('');

    for (cat in categories) {
        var simus_html = ''
        for (simu in categories[cat]['simus']) {
            // Renderear cada simulación
            var simulation = simulations[categories[cat]['simus'][simu]];
            simulation['parent'] = categories[cat].name;

            simus_html += Mustache.render($('#tmpl-simu').html(), simulation);

        }

        // Renderear categoría y agregale las simulaciones
        var html = Mustache.render($('#tmpl-category').html(), {
            'name': categories[cat]['name'],
			'fondo': categories[cat]['fondo'],
            'cant': categories[cat]['simus'].length,
            'id': cat,
            'simus': simus_html
        });
        content.append(html);
    }
}

function load_results(results){
    console.log(results)

    var simus_html = ''
    for (simus in results) {
        // Renderear cada simulación
        var simulation = simulations[results[simus]];

        simus_html += Mustache.render($('#tmpl-simu').html(), simulation);

    }

    $('section#sim-filtrar section').not('.category').remove();
    $('section#sim-filtrar').append(simus_html);
    $('section#sim-filtrar section.category span').html(results.length)

    $('section#sim-filtrar .simudescription').on('click', fn_open_simulation);

}

function fn_open_simulation(){
    open_simulation($(this));
}

function open_simulation(sim_slide){
    var sim_name = sim_slide.attr('class').match(/sim-(.*)/gi);
    $('.'+sim_name).off('click').css('cursor','wait');

    var simu_binary = sim_path + sim_slide.data('open');
    var simu_runner = java_jar;

    if (simu_binary.match(/.html$/)) {
        simu_runner = 'x-www-browser -new-window file://';
    }

    var linea_loca = simu_runner + sim_path + sim_slide.data('open')

    console.log(linea_loca);

    exec(linea_loca, function(error, stdout, stderr) {
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
    var simus_copy = simulations;
    var s_res = JSON.search(simus_copy,
                            "//*//*[contains(description, '_STR_')]//file".replace('_STR_',
                                                                             input.val()));

    load_results(
        s_res.map(function(s){ return s.replace('_es.jar', ''); })
    );

    Reveal.sync();
    setTimeout(function(){ Reveal.slide(7,0); }, 50);
}

$(document).ready(function(){
    load_simus($('#content'));
	$('#filter-sim').on("keyup", function(event) {
		if (event.keyCode === 13) {
			fn_filter_sim.call(this);
		}
	});

    $('.simudescription').on('click', fn_open_simulation);

    $('#btn-filter-sim').on('click', fn_filter_sim);

    Reveal.initialize({
        controls: true,
        progress: true,
        history: true,
        center: true,
        transition: 'slide'
    });
});
