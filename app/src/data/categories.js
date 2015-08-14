var categories = {"biologia": {"name": "Biología", "fondo": "biologia.png",
                               "simus": ["balloons",
                                         "blackbody-spectrum",
                                         "color-vision",
                                         "curve-fitting",
                                         "density",
                                         "eating-and-exercise",
                                         "gene-expression-basics",
                                         "gene-machine-lac-operon",
                                         "membrane-channels",
                                         "molecular-motors",
                                         "molecule-polarity",
                                         "mri",
                                         "natural-selection",
                                         "neuron",
                                         "optical-tweezers",
                                         "ph-scale",
                                         "plinko-probability",
                                         "radioactive-dating-game",
                                         "reactions-and-rates",
                                         "soluble-salts",
                                         "sound",
                                         "stretching-dna",
                                         "sugar-and-salt-solutions"]},
                  "fisica": {"name": "Física", "fondo": "fisica.png",
                             "simus": ["alpha-decay",
                                       "balancing-act",
                                       "balloons",
                                       "balloons-and-buoyancy",
                                       "band-structure",
                                       "battery-resistor-circuit",
                                       "battery-voltage",
                                       "bending-light",
                                       "beta-decay",
                                       "blackbody-spectrum",
                                       "bound-states",
                                       "build-an-atom",
                                       "buoyancy",
                                       "calculus-grapher",
                                       "capacitor-lab",
                                       "charges-and-fields",
                                       "circuit-construction-kit-ac",
                                       "circuit-construction-kit-ac-virtual-lab",
                                       "circuit-construction-kit-dc",
                                       "circuit-construction-kit-dc-virtual-lab",
                                       "collision-lab",
                                       "color-vision",
                                       "conductivity",
                                       "covalent-bonds",
                                       "davisson-germer",
                                       "density",
                                       "discharge-lamps",
                                       "efield",
                                       "electric-hockey",
                                       "energy-forms-and-changes",
                                       "energy-skate-park",
                                       "energy-skate-park-basics",
                                       "faraday",
                                       "faradays-law",
                                       "fluid-pressure-and-flow",
                                       "forces-1d",
                                       "forces-and-motion",
                                       "forces-and-motion-basics",
                                       "fourier",
                                       "friction",
                                       "gas-properties",
                                       "generator",
                                       "geometric-optics",
                                       "gravity-and-orbits",
                                       "gravity-force-lab",
                                       "greenhouse",
                                       "hydrogen-atom",
                                       "ladybug-motion-2d",
                                       "lasers",
                                       "lunar-lander",
                                       "magnet-and-compass",
                                       "magnets-and-electromagnets",
                                       "mass-spring-lab",
                                       "maze-game",
                                       "microwaves",
                                       "molecular-motors",
                                       "molecules-and-light",
                                       "motion-2d",
                                       "moving-man",
                                       "mri",
                                       "my-solar-system",
                                       "normal-modes",
                                       "nuclear-fission",
                                       "ohms-law",
                                       "optical-tweezers",
                                       "pendulum-lab",
                                       "photoelectric",
                                       "projectile-motion",
                                       "quantum-tunneling",
                                       "quantum-wave-interference",
                                       "radiating-charge",
                                       "radio-waves",
                                       "radioactive-dating-game",
                                       "ramp-forces-and-motion",
                                       "reactions-and-rates",
                                       "resistance-in-a-wire",
                                       "resonance",
                                       "reversible-reactions",
                                       "rotation",
                                       "rutherford-scattering",
                                       "semiconductor",
                                       "signal-circuit",
                                       "sound",
                                       "states-of-matter",
                                       "states-of-matter-basics",
                                       "stern-gerlach",
                                       "stretching-dna",
                                       "the-ramp",
                                       "torque",
                                       "travoltage",
                                       "under-pressure",
                                       "wave-interference",
                                       "wave-on-a-string"]},
                  "inv": {"name": "Investigaciones avanzadas", "fondo": "avanzadas.png",
                          "simus": ["lasers",
                                    "molecular-motors",
                                    "optical-quantum-control",
                                    "optical-tweezers",
                                    "self-driven-particle-model",
                                    "stretching-dna"]},
                  "matematica": {"name": "Matemática", "fondo": "matematica.png",
                                 "simus": ["area-builder",
                                           "arithmetic",
                                           "balancing-act",
                                           "build-a-fraction",
                                           "calculus-grapher",
                                           "curve-fitting",
                                           "equation-grapher",
                                           "estimation",
                                           "fourier",
                                           "fraction-matcher",
                                           "fractions-intro",
                                           "graphing-lines",
                                           "mass-spring-lab",
                                           "moving-man",
                                           "ohms-law",
                                           "pendulum-lab",
                                           "plinko-probability",
                                           "projectile-motion",
                                           "resistance-in-a-wire",
                                           "rotation",
                                           "vector-addition"]},
                  "nuevas": {"name": "Nuevas Simulaciones", "fondo": "nuevas.png",
                             "simus": ["area-builder",
                                       "balancing-act",
                                       "beers-law-lab",
                                       "build-a-fraction",
                                       "concentration",
                                       "energy-forms-and-changes",
                                       "energy-skate-park-basics",
                                       "fluid-pressure-and-flow",
                                       "forces-and-motion-basics",
                                       "fraction-matcher",
                                       "fractions-intro",
                                       "gene-expression-basics",
                                       "graphing-lines",
                                       "molarity",
                                       "molecule-polarity",
                                       "molecule-shapes",
                                       "molecule-shapes-basics",
                                       "normal-modes",
                                       "plate-tectonics",
                                       "radiating-charge",
                                       "states-of-matter-basics",
                                       "sugar-and-salt-solutions",
                                       "under-pressure"]},
                  "quimica": {"name": "Química", "fondo": "quimica.png",
                              "simus": ["acid-base-solutions",
                                        "alpha-decay",
                                        "atomic-interactions",
                                        "balancing-chemical-equations",
                                        "balloons",
                                        "balloons-and-buoyancy",
                                        "beers-law-lab",
                                        "beta-decay",
                                        "blackbody-spectrum",
                                        "build-a-molecule",
                                        "build-an-atom",
                                        "concentration",
                                        "density",
                                        "discharge-lamps",
                                        "gas-properties",
                                        "greenhouse",
                                        "hydrogen-atom",
                                        "isotopes-and-atomic-mass",
                                        "microwaves",
                                        "molarity",
                                        "molecule-polarity",
                                        "molecule-shapes",
                                        "molecule-shapes-basics",
                                        "molecules-and-light",
                                        "nuclear-fission",
                                        "ph-scale",
                                        "ph-scale-basics",
                                        "photoelectric",
                                        "radio-waves",
                                        "radioactive-dating-game",
                                        "reactants-products-and-leftovers",
                                        "reactions-and-rates",
                                        "reversible-reactions",
                                        "rutherford-scattering",
                                        "soluble-salts",
                                        "states-of-matter",
                                        "states-of-matter-basics",
                                        "sugar-and-salt-solutions",
                                        "wave-on-a-string"]},
                  "tierra": {"name": "Ciencias de la Tierra", "fondo": "tierra.png",
                             "simus": ["balloons",
                                       "balloons-and-buoyancy",
                                       "blackbody-spectrum",
                                       "fluid-pressure-and-flow",
                                       "gas-properties",
                                       "glaciers",
                                       "gravity-and-orbits",
                                       "greenhouse",
                                       "molecules-and-light",
                                       "my-solar-system",
                                       "ph-scale",
                                       "plate-tectonics",
                                       "radioactive-dating-game",
                                       "sound",
                                       "under-pressure",
                                       "wave-interference",
                                       "wave-on-a-string"]
                            },
                  "filtrar": {"name": "Resultados de búsqueda", "fondo": "buscar.png",
                              "simus": []
                             }
                 }
