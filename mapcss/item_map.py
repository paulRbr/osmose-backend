#-*- coding: utf-8 -*-
item_map = \
{'DutchSpecific': {'class': {None: 0,
                             'NL German style tagging': 6,
                             'NL addresses and contacts': 1,
                             'NL deprecated features': 2,
                             'NL heritage': 4,
                             'NL mofa tagging': 8,
                             'NL nomenclature': 3,
                             'NL speed limits': 7,
                             'NL traffic signs': 5},
                   'item': 9020,
                   'only_for': ['NL-ZH',
                                'NL-ZE',
                                'NL-NB',
                                'NL-LI',
                                'NL-GE',
                                'NL-OV',
                                'NL-DR',
                                'NL-FR',
                                'NL-GR',
                                'NL-FL',
                                'NL-UT',
                                'NL-NH'],
                   'prefix': 'Josm_',
                   'url': 'https://raw.githubusercontent.com/Famlam/OsmMapcssValidationNL/main/netherlands.validator.mapcss',
                   'url_display': 'https://github.com/Famlam/OsmMapcssValidationNL/blob/main/netherlands.validator.mapcss'},
 'FranceSpecificRules': {'class': {None: 0,
                                   "Unusual ref for motorway_junction; use of 'ref=*' for the exit destination ref?": 9019004,
                                   'missing tag': 9019003,
                                   'validation rules highway milestone': 9019001,
                                   'validation rules nat_ref in France': 9019002},
                         'item': 9019,
                         'only_for': ['FR'],
                         'prefix': 'Josm_',
                         'tags': [],
                         'url': 'https://josm.openstreetmap.de/josmfile?page=Rules/FranceSpecificRules',
                         'url_display': 'https://josm.openstreetmap.de/wiki/Rules/FranceSpecificRules'},
 'ItalySpecific': {'class': {None: 0},
                   'only_for': ['IT'],
                   'prefix': 'Josm_',
                   'url': 'https://josm.openstreetmap.de/josmfile?page=Rules/ItalySpecific',
                   'url_display': 'https://josm.openstreetmap.de/wiki/Rules/ItalySpecific'},
 'Rules_Brazilian-Specific': {'class': {'Brasil - Correções e melhorias': 9018006,
                                        'Brasil - Verificar': 9018002,
                                        'SAMU classificado de forma errada': 9018016,
                                        'adicionar {0} ao {1}': 9018018,
                                        'ausência de "{0}" na {1}': 9018054,
                                        'ausência de boundary=protected_area': 9018035,
                                        'ausência do tempo de duração ({0}) da balsa': 9018027,
                                        'ausência do tipo de serviço ({0}) na {1}': 9018060,
                                        'ausência do tipo de torre ({0})': 9018024,
                                        'ausência do tipo de track ({0}) na {1}': 9018061,
                                        'chave inválida: {0}': 9018022,
                                        "especificar valor correto para {0} ao invés de ''{1}''": 9018021,
                                        'link sem tag {0}': 9018055,
                                        'nome supérfluo/incompleto de local de lazer': 9018004,
                                        'nome supérfluo/incompleto de local de saúde': 9018005,
                                        'nome utilizado de forma incorreta': 9018031,
                                        'não classificar via como {0}': 9018051,
                                        'não se deve utilizar {0} para demarcar áreas de cobertura de imagem': 9018023,
                                        "não utilizar ''{0}'' para locais sem número": 9018043,
                                        'nó não deve possuir {0}': 9018032,
                                        'o conteúdo de {0} deve fazer parte de ref, separado por ;': 9018039,
                                        'objeto com nomenclatura incorreta': 9018007,
                                        'objeto contém Google como source': 9018044,
                                        'objeto incompleto: possui apenas {0}': 9018041,
                                        'objeto incompleto: possui apenas {0} e {1}': 9018042,
                                        'objeto não deve possuir {0}': 9018017,
                                        'palavra abreviada em {0}': 9018003,
                                        'possível ausência de tag {0}': 9018026,
                                        "possível definição incorreta para praça: ''{0}''": 9018029,
                                        'postos/unidades de saúde devem ser amenity=clinic': 9018015,
                                        'relação não deve possuir {0}': 9018046,
                                        'rodovia com ref no nome': 9018045,
                                        'uso incorreto de {0}': 9018064,
                                        'uso incorreto de {0} com {1}': 9018063,
                                        'utilizar ; como separador de valores em {0}': 9018040,
                                        'utilizar prefixo em português (pt:) para {0}': 9018030,
                                        'utilizar {0} apenas em {1}={2}': 9018065,
                                        "utilize ''destination'' no caminho de saída ao invés de ''exit_to''": 9018037,
                                        'valor incorreto para {0}': 9018034,
                                        '{0} com logradouro ausente, errado ou abreviado': 9018001,
                                        '{0} com nome supérfluo/incompleto': 9018052,
                                        '{0} com valor = {1}': 9018014,
                                        '{0} com {1}': 9018062,
                                        '{0} deve conter apenas o nome da cidade': 9018013,
                                        "{0} deve estar incluído em {1}, separado por '';'' caso necessário": 9018020,
                                        "{0} deve possuir ''type=boundary''": 9018048,
                                        '{0} deve possuir {1}': 9018033,
                                        '{0} deve ser usado apenas em ways': 9018036,
                                        '{0} deve ser utilizado apenas em nós': 9018047,
                                        '{0} deve ser utilizado apenas no nó de saída da rodovia': 9018056,
                                        '{0} deve ser utilizado com {1}={0} ou {2}={0}': 9018019,
                                        '{0} deve ser utilizado junto com {1}': 9018049,
                                        '{0} e {1} são iguais; adicionar nome completo da rodovia': 9018050,
                                        '{0} não deve possuir {1}': 9018053,
                                        '{0} não deve ser utilizado em nó; utilizar a restrição na via': 9018008,
                                        '{0} sem nome': 9018012,
                                        '{0} sem número de faixas ({1}) definido': 9018058,
                                        '{0} sem pelo menos uma das tags: {1} ou {2}': 9018010,
                                        '{0} sem superfície ({1}) definida': 9018057,
                                        '{0} sem tag de acessibilidade ({1})': 9018028,
                                        '{0} sem tag de população (population)': 9018011,
                                        '{0} sem tag {1}': 9018025,
                                        '{0} sem velocidade máxima ({1}) definida': 9018059,
                                        '{0} sem {1}': 9018038,
                                        '{0} é uma chave utilizada apenas no Reino Unido': 9018009},
                              'item': 9018,
                              'only_for': ['BR'],
                              'prefix': 'Josm_',
                              'subclass_blacklist': [339470124,
                                                     995006835,
                                                     1594044971,
                                                     226394604,
                                                     2012241162,
                                                     1322492249,
                                                     1123790420,
                                                     951501764,
                                                     1948798798,
                                                     733725137,
                                                     2074305530,
                                                     282605167,
                                                     39095837,
                                                     1154433213,
                                                     1415734409,
                                                     58812649,
                                                     1354724892,
                                                     2146320716,
                                                     1840875080,
                                                     1508736498,
                                                     877403916,
                                                     1322492249,
                                                     481849808,
                                                     1279481357,
                                                     200264401,
                                                     200264401],
                              'tags': ['tag'],
                              'url': 'https://raw.githubusercontent.com/OSMBrasil/validador-josm/master/Rules_Brazilian-Specific.validator.mapcss',
                              'url_display': 'https://github.com/OSMBrasil/validador-josm/blob/master/Rules_Brazilian-Specific.validator.mapcss'},
 'Seamark': {'class': {'In {0} {1}={2} require {3}={4}': 9012009,
                       'Multi-colour {0} without {1}': 9012001,
                       'Probably wrong category on {0}, the colour combination {1} usually mean {2}': 9012005,
                       'Probably wrong category on {0}, {1} colour mean {2} in {3}': 9012004,
                       'Unrecognized {0}: {1}': 9012002,
                       '{0} have no IALA or system defind ({1})': 9012003,
                       '{0} have no {1}': 9012006,
                       '{0} set without {1}={2}': 9012007,
                       '{0} sign require {1} set to left or right': 9012010,
                       '{0} without {1}': 9012008},
             'item': 9012,
             'prefix': 'Josm_',
             'tags': ['tag', 'seamark'],
             'url': 'https://raw.githubusercontent.com/OpenNauticalChart/josm/master/Seamark.validator.mapcss',
             'url_display': 'https://github.com/OpenNauticalChart/josm/blob/master/Seamark.validator.mapcss'},
 'SuspiciousSwimming_Pool': {'class': {'If this is a facility containing one or more swimming pools it should be tagged leisure=sports_centre + sport=swimming.': 30801},
                             'item': 3080,
                             'prefix': 'Josm_',
                             'tags': ['tag'],
                             'url': 'https://josm.openstreetmap.de/josmfile?page=Rules/SuspiciousSwimming_Pool',
                             'url_display': 'https://josm.openstreetmap.de/wiki/Rules/SuspiciousSwimming_Pool'},
 'addresses': {'class': {'Object has no {0}, however, it has {1} and {2} whose value looks like a housenumber.': 9000002,
                         'Same value of {0} and {1}': 9000003,
                         'Way with {0}. Tag each housenumber separately if possible.': 9000001,
                         '{0} without number': 9000004},
               'item': 9000,
               'not_for': ['CA'],
               'prefix': 'Josm_',
               'tags': ['tag', 'addr'],
               'url': 'https://josm.openstreetmap.de/browser/josm/trunk/resources/data/validator/addresses.mapcss?format=txt',
               'url_display': 'https://josm.openstreetmap.de/browser/josm/trunk/resources/data/validator/addresses.mapcss'},
 'combinations': {'class': {'Use {0} only as value of {1}': 9001005,
                            'incomplete usage of {0} on a way without {1}': 9001004,
                            'missing tag': 9001001,
                            'suspicious tag combination': 9001002,
                            '{0} on a relation without {1}': 9001003},
                  'item': 9001,
                  'prefix': 'Josm_',
                  'tags': ['tag'],
                  'url': 'https://josm.openstreetmap.de/browser/josm/trunk/resources/data/validator/combinations.mapcss?format=txt',
                  'url_display': 'https://josm.openstreetmap.de/browser/josm/trunk/resources/data/validator/combinations.mapcss'},
 'de-openrailwaymap': {'class': {"German Ks signals can't have main and distant signal at the same place, try a combined signal instead": 9016009,
                                 "German distant signals can't be repeated and shortened at the same time": 9016008,
                                 'It is unclear if Zs10 light signals have ever been placed, please double check.': 9016016,
                                 'KVB hp signals only exist as light signals': 9016003,
                                 'Ne 14 sign requires additional tag railway:signal:train_protection:type=block_marker': 9016006,
                                 'Sh light signals cannot display Sh 0, but only Hp 0': 9016011,
                                 'Sh semaphore signals cannot display Hp 0, but only Sh 0': 9016010,
                                 'Signal Gsp 2 was renamed to Wn 7 in 2008': 9016005,
                                 'Track names should be real names. KBS numbers should be mapped as a relation with route=railway, track numbers as railway:track_ref=*.': 9016024,
                                 'Track names should be real names. KBS numbers should be mapped as a relation with route=railway.': 9016023,
                                 'Track names should be real names. VzG numbers should be tagged ref=*. KBS numbers should be mapped as a relation with route=railway.': 9016022,
                                 'Track refs should be VzG numbers in Germany. KBS numbers should be mapped as a relation with route=railway, track numbers as railway:track_ref=*.': 9016026,
                                 'Track refs should be VzG numbers in Germany. KBS numbers should be mapped as a relation with route=railway.': 9016025,
                                 'Tracks should not be named by their timetable number (KBS xy). Use a route relation with route=railway, instead.': 9016017,
                                 'Vr repeated signals only exist as light signals': 9016004,
                                 'VzG numbers should be tagged as ref=* without "VzG"': 9016020,
                                 "Zs3 light signal states should have the form 'speed[;speed …][;off][;?], speeds can only be multiples of 10": 9016015,
                                 'Zs3 sign signals can only have a single speed, are a multiple of 5 and cannot be greater than 160': 9016013,
                                 "Zs3v light signal states should have the form 'speed[;speed …][;off][;?], speeds can only be multiples of 10": 9016014,
                                 'Zs3v sign signals can only have a single speed, are a multiple of 5 and cannot be greater than 160': 9016012,
                                 'hp signals only exist as semaphore or light signals': 9016002,
                                 'main and repeated distant signal usually are not at the same place': 9016007,
                                 "mapcss._tag_uncapture(capture_tags, 'workrules={1.value} is deprecated, change to workrules=DE:{1.value}')": 9016031,
                                 "mapcss._tag_uncapture(capture_tags, '{1.value} signals only exist as light signals')": 9016030,
                                 "mapcss._tag_uncapture(capture_tags, u'workrules={1.value} is deprecated, change to workrules=DE:{1.value}')": 9016027,
                                 "mapcss._tag_uncapture(capture_tags, u'{1.value} signals only exist as light signals')": 9016001,
                                 'ref=* should be a VzG number (without "VzG"). Use a route relation with route=railway for KBS numbers, instead.': 9016018,
                                 'ref=* should be a VzG number without "VzG"': 9016019,
                                 'ref=* should only be a VzG number, it should not contain the track number': 9016021,
                                 'workrules: separate country and ruleset by : , not by -': 9016029,
                                 'workrules=BOA is deprecated, replace by an adequate value': 9016028},
                       'item': 9016,
                       'only_for': ['DE'],
                       'prefix': 'Josm_',
                       'tags': ['tag', 'railway'],
                       'url': 'https://www.openrailwaymap.org/validator/de-openrailwaymap.validator.mapcss'},
 'deprecated': {'class': {"''{0}'' does not specify the official mode of transportation, use ''{1}'' for example": 9002003,
                          "''{0}'' is meaningless, use more specific tags, e.g. ''{1}''": 9002002,
                          'The key {0} has an uncommon value.': 9002017,
                          'Unspecific tag {0}': 9002010,
                          'Unusual key {0}, maybe {1} or {2} is meant': 9002021,
                          'Wrong usage of {0} tag. Remove {1}, because it is clear that the name is missing even without an additional tag.': 9002005,
                          'deprecated tagging': 9002001,
                          'key with uncommon character': 9002011,
                          'misspelled value': 9002018,
                          'questionable key (ending with a number)': 9002014,
                          'uncommon short key': 9002012,
                          'unusual value of {0}': 9002020,
                          'wrong value: {0}': 9002019,
                          '{0} = {1}; remove {0}': 9002009,
                          '{0} as a tag on an object. Roles are specified in the relation members list instead.': 9002022,
                          '{0} is inaccurate. Use separate tags for each specific type, e.g. {1} or {2}.': 9002013,
                          '{0} is not recommended. Use the Reverse Ways function from the Tools menu.': 9002016,
                          '{0} is unspecific': 9002024,
                          '{0} is unspecific. Instead use the key fixme with the information what exactly should be fixed in the value of fixme.': 9002006,
                          '{0} should be replaced with {1}': 9002008,
                          '{0} with a temporary URL which may be outdated very soon': 9002023,
                          "{0}={1} is unspecific. Instead of ''{1}'' please give more information about what exactly should be fixed.": 9002004,
                          "{0}={1} is unspecific. Please replace ''{1}'' by ''left'', ''right'' or ''both''.": 9002015,
                          "{0}={1} is unspecific. Please replace ''{1}'' by a specific value.": 9002007},
                'item': 9002,
                'prefix': 'Josm_',
                'subclass_blacklist': [740601387, 512779280],
                'tags': ['tag', 'deprecated'],
                'url': 'https://josm.openstreetmap.de/browser/josm/trunk/resources/data/validator/deprecated.mapcss?format=txt',
                'url_display': 'https://josm.openstreetmap.de/browser/josm/trunk/resources/data/validator/deprecated.mapcss'},
 'geometry': {'class': {'Object at Position 0.00E 0.00N. There is nothing at this position except an already mapped weather buoy.': 9003009,
                        'Way with {0} not closed.': 9003010,
                        'suspicious tag combination': 9003005,
                        '{0} on a closed way. Should be used on an unclosed way.': 9003011,
                        '{0} on a node': 9003006,
                        '{0} on a node. Should be drawn as an area.': 9003003,
                        '{0} on a node. Should be used in a relation': 9003004,
                        '{0} on a node. Should be used on a way or relation.': 9003002,
                        '{0} on a node. Should be used on a way.': 9003001,
                        '{0} on a relation': 9003012,
                        '{0} on a way. Should be used in a relation': 9003008,
                        '{0} on a way. Should be used on a node.': 9003007},
              'item': 9003,
              'prefix': 'Josm_',
              'tags': ['geom'],
              'url': 'https://josm.openstreetmap.de/browser/josm/trunk/resources/data/validator/geometry.mapcss?format=txt',
              'url_display': 'https://josm.openstreetmap.de/browser/josm/trunk/resources/data/validator/geometry.mapcss'},
 'highway': {'class': {'Unnamed unclassified highway': 9004003,
                       'Unspecific highway type': 9004004,
                       "Value of ''{0}'' should either be ''{1}'' or ''{2}''. For sidewalks use ''{3}'' instead.": 9004007,
                       'abbreviated street name': 9004001,
                       'deprecated tagging': 9004006,
                       'missing tag': 9004009,
                       'questionable value (ending with a number)': 9004012,
                       'suspicious tag combination': 9004011,
                       'unusual value of {0}': 9004014,
                       'wrong crossing tag on a way': 9004002,
                       'wrong highway tag on a node': 9004008,
                       '{0} on a node': 9004010,
                       '{0} together with {1}': 9004013,
                       '{0} used with {1}': 9004005},
             'item': 9004,
             'prefix': 'Josm_',
             'subclass_blacklist': [1472864339],
             'tags': ['tag', 'highway'],
             'url': 'https://josm.openstreetmap.de/browser/josm/trunk/resources/data/validator/highway.mapcss?format=txt',
             'url_display': 'https://josm.openstreetmap.de/browser/josm/trunk/resources/data/validator/highway.mapcss'},
 'multiple': {'class': {"empty value in semicolon-separated ''{0}''": 9005002,
                        '{0} with multiple values': 9005001},
              'item': 9005,
              'prefix': 'Josm_',
              'tags': ['tag', 'value'],
              'url': 'https://josm.openstreetmap.de/browser/josm/trunk/resources/data/validator/multiple.mapcss?format=txt',
              'url_display': 'https://josm.openstreetmap.de/browser/josm/trunk/resources/data/validator/multiple.mapcss'},
 'numeric': {'class': {'Airport tagging': 9006022,
                       'Definition of {0} is unclear': 9006027,
                       'Unnecessary amount of decimal places': 9006021,
                       'imprecise value of {0}': 9006029,
                       'negative {0} value': 9006023,
                       'numerical key': 9006001,
                       'suspicious tag combination': 9006030,
                       'unnecessary tag': 9006025,
                       'unusual value of {0}': 9006010,
                       'unusual value of {0}: kilometers is default; point is decimal separator; if units, put space then unit': 9006020,
                       'unusual value of {0}: meters is default; point is decimal separator; if units, put space then unit': 9006018,
                       'unusual value of {0}: set unit e.g. {1} or {2}; only positive values; point is decimal separator; space between value and unit': 9006028,
                       'unusual value of {0}: tonne is default; point is decimal separator; if units, put space then unit': 9006019,
                       'unusual value of {0}: use . instead of , as decimal separator': 9006017,
                       'unusual value of {0}: use abbreviation for unit and space between value and unit': 9006024,
                       'unusual value of {0}: {1} is default; only positive values; point is decimal separator; if units, put space then unit': 9006026,
                       'voltage should be in volts with no units/delimiter/spaces': 9006013,
                       '{0} must be a numeric value': 9006008,
                       '{0} must be a numeric value, in meters and without units': 9006011,
                       '{0} must be a positive integer number': 9006009,
                       '{0} should be an integer value between -5 and 5': 9006003,
                       '{0} should have numbers only with optional .5 increments': 9006004,
                       '{0} value with + sign': 9006002},
             'item': 9006,
             'prefix': 'Josm_',
             'tags': ['tag', 'value'],
             'url': 'https://josm.openstreetmap.de/browser/josm/trunk/resources/data/validator/numeric.mapcss?format=txt',
             'url_display': 'https://josm.openstreetmap.de/browser/josm/trunk/resources/data/validator/numeric.mapcss'},
 'openrailwaymap': {'class': {'A sign cannot have different states.': 9015031,
                              'Crossings and level crossings should be mapped as nodes': 9015017,
                              'If tracks are tagged with service=*, they should be mapped as one way per track.': 9015016,
                              'Key traffic_mode is deprecated': 9015004,
                              'Milestone without position, add railway:position=*': 9015028,
                              'Station mapped as a way, but should be mapped as a node': 9015002,
                              'Tagging for resetting switch is deprecated, change railway:switch=* to proper value': 9015040,
                              'Track tagged with usage=* AND service=* - remove one of these tags': 9015001,
                              'Track without operator': 9015003,
                              'Track without workrules': 9015006,
                              'controlled_area relations are deprecated': 9015041,
                              'interlocking relation with type other than railway': 9015043,
                              'interlocking relation without type=railway': 9015042,
                              'lanes=* is used for highways, not railways': 9015024,
                              'main and combined signal at the same place': 9015035,
                              'maxspeed should contain the value as it is shown on the line with mph as unit': 9015026,
                              'maxspeed=signals is deprecated, tag the highest possible speed instead': 9015025,
                              "platform names or refs should not include the word 'track', write that as 'description', put the bare numbers in 'ref', separated by ';'": 9015010,
                              'platforms should have the numbers in ref, not railway:track_ref': 9015008,
                              'power:type is deprecated, change to proper electrified value': 9015013,
                              'power:type=overhead is deprecated': 9015011,
                              'power:type=overhead is deprecated, conflict between {0} and {1}': 9015012,
                              'priority on railway objects is deprecated, remove it': 9015014,
                              'radio=* is deprecated, change to proper railway:radio value': 9015019,
                              'radio=GSM-R is deprecated': 9015018,
                              'railway:signal:stop:description is deprecated and has been replaced by railway:signal:stop:caption': 9015033,
                              'railway:signal:stop:description is deprecated, replace by appropiate railway:signal:stop:caption value': 9015034,
                              'railway=flat_crossing is deprecated': 9015032,
                              'signal names should be prefixed with an operator or country prefix': 9015038,
                              'signal specification given but node is not tagged as signal or equivalent type': 9015030,
                              'signals should be tagged with ref, not railway:ref': 9015036,
                              'signals should have a railway:signal:direction=* tag': 9015037,
                              'supervised=* is deprecated': 9015029,
                              "track names or refs should not include the word 'track', tag those numbers as railway:track_ref": 9015009,
                              'track numbers inside a station should be railway:track_ref, not name': 9015007,
                              'track numbers inside a station should be railway:track_ref, not ref': 9015045,
                              "track tagged with 'bridge' in name, consider using bridge:name instead and put the track name into name": 9015022,
                              "track tagged with 'bridge' in wikipedia, consider using bridge:wikipedia instead and put track wikipedia entry into wikipedia": 9015023,
                              "track tagged with 'tunnel' in name, consider using tunnel:name instead and put the track name into name": 9015020,
                              "track tagged with 'tunnel' in wikipedia, consider using tunnel:wikipedia instead and put the track wikipedia entry into wikipedia": 9015021,
                              'tracks=1 not necessary if detail=track is tagged.': 9015015,
                              'usage=freight is deprecated': 9015005,
                              '{0} identification should be tagged as ref, not as name': 9015039,
                              '{0}={1} without name': 9015044,
                              '{0}={1} without {2}:railway': 9015027},
                    'item': 9015,
                    'prefix': 'Josm_',
                    'subclass_blacklist': [160705788, 321695123],
                    'tags': ['tag', 'railway'],
                    'url': 'https://www.openrailwaymap.org/validator/openrailwaymap.validator.mapcss'},
 'relation': {'class': {'missing tag': 9007001,
                        'relation without type': 9007002},
              'item': 9007,
              'prefix': 'Josm_',
              'tags': ['tag', 'relation'],
              'url': 'https://josm.openstreetmap.de/browser/josm/trunk/resources/data/validator/relation.mapcss?format=txt',
              'url_display': 'https://josm.openstreetmap.de/browser/josm/trunk/resources/data/validator/relation.mapcss'},
 'religion': {'class': {'missing tag': 9008001,
                        'unknown christian denomination': 9008002,
                        'unknown jewish denomination': 9008004,
                        'unknown muslim denomination': 9008003,
                        '{0}': 9008005},
              'item': 9008,
              'prefix': 'Josm_',
              'tags': ['tag'],
              'url': 'https://josm.openstreetmap.de/browser/josm/trunk/resources/data/validator/religion.mapcss?format=txt',
              'url_display': 'https://josm.openstreetmap.de/browser/josm/trunk/resources/data/validator/religion.mapcss'},
 'ru-housenumber': {'class': {'Номера домов не соответствующие принятому соглашению': 9017001},
                    'item': 9017,
                    'only_for': ['RU'],
                    'prefix': 'Josm_',
                    'tags': ['tag', 'addr'],
                    'url': 'https://raw.githubusercontent.com/zetx16/Josm-HnumbValidator/master/ru-housenumber.validator.mapcss',
                    'url_display': 'https://github.com/zlant/Josm-HnumbValidator/blob/master/ru-housenumber.validator.mapcss'},
 'territories': {'class': {'deprecated tagging': 9009001,
                           'street name contains ss': 9009002,
                           'street name contains ß': 9009003},
                 'item': 9009,
                 'prefix': 'Josm_',
                 'tags': ['tag'],
                 'url': 'https://josm.openstreetmap.de/browser/josm/trunk/resources/data/validator/territories.mapcss?format=txt',
                 'url_display': 'https://josm.openstreetmap.de/browser/josm/trunk/resources/data/validator/territories.mapcss'},
 'transport': {'class': {'A bus stop is supposed to be a node': 9014019,
                         'Check if the note can be deleted': 9014006,
                         'Check the network tag': 9014014,
                         'Check the network tag : this network does not exist, it may be a typo': 9014026,
                         'Check the operator tag': 9014013,
                         'Check the operator tag : this operator does not exist, it may be a typo': 9014025,
                         'Is it a bus stop or a bus station?': 9014002,
                         'Missing from/to tag on a public_transport route relation': 9014018,
                         'Missing interval tag to specify the main interval': 9014023,
                         'Missing legacy tag on a public transport stop': 9014004,
                         'Missing network tag on a public_transport relation': 9014015,
                         'Missing opening_hours tag': 9014024,
                         'Missing operator tag on a public_transport relation': 9014016,
                         'Missing public_transport tag on a public transport stop': 9014003,
                         'Missing public_transport:version tag on a public_transport route relation': 9014011,
                         'Missing ref tag for line number on a public_transport relation': 9014017,
                         'Missing transportation mode, add a tag route = bus/coach/tram/etc': 9014009,
                         'Missing transportation mode, change tag route to route_master': 9014010,
                         'Stop without name': 9014001,
                         'Subway entrances should be mapped as nodes': 9014027,
                         'The color of the public transport line should be in a colour tag': 9014020,
                         'The duration is invalid (try a number of minutes)': 9014022,
                         'The interval is invalid (try a number of minutes)': 9014021,
                         'The line variant does not belong to any line, add it to the route_master relation': 9014028,
                         'The network should be on the transport lines and not on the stops': 9014007,
                         'The operator should be on the transport lines and not on the stops': 9014008,
                         'The stops may not be in the right order': 9014012},
               'item': 9014,
               'prefix': 'Josm_',
               'tags': ['tag', 'public_transport'],
               'url': 'https://raw.githubusercontent.com/Jungle-Bus/transport_mapcss/master/transport.validator.mapcss',
               'url_display': 'https://github.com/Jungle-Bus/transport_mapcss/blob/master/transport.validator.mapcss'},
 'unnecessary': {'class': {'descriptive name': 9010003,
                           'unnecessary tag': 9010001,
                           '{0} makes no sense': 9010002},
                 'item': 9010,
                 'prefix': 'Josm_',
                 'tags': ['tag'],
                 'url': 'https://josm.openstreetmap.de/browser/josm/trunk/resources/data/validator/unnecessary.mapcss?format=txt',
                 'url_display': 'https://josm.openstreetmap.de/browser/josm/trunk/resources/data/validator/unnecessary.mapcss'},
 'wikipedia': {'class': {"''{0}'' tag is set, but no ''{1}'' tag. Make sure to set ''wikipedia=language:value'' for the main article and optional ''wikipedia:language=value'' only for additional articles that are not just other language variants of the main article.": 9011015,
                         'deprecated tagging': 9011003,
                         'missing tag': 9011013,
                         'wikidata tag must be in Qnnnn format, where n is a digit': 9011012,
                         "wikipedia ''{0}'' language is invalid, use ''{1}'' instead": 9011005,
                         "wikipedia ''{0}'' language is obsolete, use ''{1}'' instead": 9011004,
                         'wikipedia language seems to be duplicated, e.g. en:en:Foo': 9011011,
                         'wikipedia page title should have first letter capitalized': 9011009,
                         "wikipedia page title should have spaces instead of underscores (''_''→'' '')": 9011010,
                         'wikipedia tag has an unknown language prefix': 9011002,
                         "wikipedia tag has no language given, use ''wikipedia''=''language:page title''": 9011001,
                         "wikipedia tag is not set, but a ''{0}'' tag is. Make sure to use wikipedia=language:value together with wikidata tag.": 9011014,
                         "wikipedia title should not have ''{0}'' prefix": 9011008,
                         'wikipedia title should not start with a space after language code': 9011007,
                         "{0} tag should not have URL-encoded values like ''%27''": 9011006,
                         '{0} value looks like a {1} value': 9011016},
               'item': 9011,
               'prefix': 'Josm_',
               'tags': ['tag', 'wikipedia'],
               'url': 'https://josm.openstreetmap.de/browser/josm/trunk/resources/data/validator/wikipedia.mapcss?format=txt',
               'url_display': 'https://josm.openstreetmap.de/browser/josm/trunk/resources/data/validator/wikipedia.mapcss'}}
