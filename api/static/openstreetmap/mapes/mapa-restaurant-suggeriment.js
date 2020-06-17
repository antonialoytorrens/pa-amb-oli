function carregaMapa() {
    var straitSource;
    var map;
    content = document.getElementById('popup-content');
    var lat = 39.62146;
    var lon = 2.91229;
    var center = ol.proj.transform([lon, lat], 'EPSG:4326', 'EPSG:3857'); //initial position of map
    var view = new ol.View({
        center: center,
        zoom: 10
    });

    //raster layer on map
    var OSMBaseLayer = new ol.layer.Tile({
        source: new ol.source.OSM()
    });

    straitSource = new ol.source.Vector({ wrapX: true });
    var straitsLayer = new ol.layer.Vector({
        source: straitSource
    });

    map = new ol.Map({
        layers: [OSMBaseLayer, straitsLayer],
        target: 'map',
        view: view,
        controls: [new ol.control.FullScreen(), new ol.control.Zoom(), ]
    });

    // Popup showing the position the user clicked
    var container = document.getElementById('popup');
    var popup = new ol.Overlay({
        element: container,
        autoPan: true,
        autoPanAnimation: {
            duration: 250
        }
    });
    map.addOverlay(popup);

    /* Add a pointermove handler to the map to render the popup.*/
    map.on('click', function(evt) {
        var feature = map.forEachFeatureAtPixel(evt.pixel, function(feat, layer) {
            return feat;
        });

        if (feature && feature.get('type') == 'Point') {
            var coordinate = evt.coordinate; //default projection is EPSG:3857 you may want to use ol.proj.transform

            content.innerHTML = feature.get('desc');
            //document.getElementById("cont").innerHTML+="Hola, "
            popup.setPosition(coordinate);
        } else {
            popup.setPosition(undefined);

        }
    });

    //var data = [];
    function addData() {

        // Respecte al mapa, la plantilla també ve donada per ajax

        $.ajax({
            type: "GET",
            url: "/restaurants/mapa/",
            dataType: "json",
            success: function(response) {
                var data = [];
                //console.log(response)
                for (i in response.restaurants) {
                    var json = {};
                    json.id = response.restaurants[i].id;
                    json.Nom = response.restaurants[i].nom;
                    json.Descripcio = response.restaurants[i].descripcio;
                    json.Lon = parseFloat(response.restaurants[i].longitud);
                    json.Lat = parseFloat(response.restaurants[i].latitud);
                    json.visible = response.restaurants[i].visible;
                    //console.log(json)
                    data.push(json);
                }
                //console.log(data);

                // ADD GEOMETRY POINT TO MAP
                data.forEach(function(item) { //iterate through array...
                    //var link = '<a href="/restaurants/?id=' + id + '"#restaurant-seleccionat>Veure detalls del restaurant</a>';
                    //console.log(link);
                    var visible = item.visible;
                    if (visible) {
                        var id = item.id;
                        var nom = item.Nom;
                        var info = item.Descripcio;
                        var descripcio = (info.length > 40) ? info.substring(0, 40) + '...' : info;
                        var longitude = item.Lon,
                            latitude = item.Lat,
                            iconFeature = new ol.Feature({
                                geometry: new ol.geom.Point(ol.proj.transform([longitude, latitude], 'EPSG:4326',
                                    'EPSG:3857')),
                                type: 'Point',
                                desc: '<pre> <b>' + nom + ' </b> ' + '<br>' + descripcio + '<br>' + '<a href="/suggeriments/actualitza-restaurant/?id=' + id + '#restaurant-seleccionat">Veure detalls del restaurant</a>' + '</pre>'
                            }),
                            iconStyle = new ol.style.Style({
                                image: new ol.style.Circle({
                                    radius: 5,
                                    stroke: new ol.style.Stroke({
                                        color: 'blue'
                                    }),
                                    fill: new ol.style.Fill({
                                        color: [57, 228, 193, 0.84]
                                    }),
                                })
                            });

                        iconFeature.setStyle(iconStyle);

                        straitSource.addFeature(iconFeature);
                    }
                });
            },
            error: function(response) {
                console.log(response)
            }
        });
    }
    //data+=[{"Nom":"Lorem Ipsum", "Descripcio":"Lorem Ipsum", "Lon":2.91458,"Lat":39.72255}, {"Nom":"Lorem Ipsum2", "Descripcio":"Lorem Ipsum", "Lon":19.455128,"Lat":41.310575},{"Nom":"Lorem Ipsum3", "Descripcio":"Lorem Ipsum", "Lon":19.455128,"Lat":41.310574},{"Nom":"Lorem Ipsum4", "Descripcio":"Lorem Ipsum", "Lon":19.457388,"Lat":41.300442},{"Nom":"Lorem Ipsum5", "Descripcio":"Lorem Ipsum", "Lon":19.413507,"Lat":41.295189},{"Nom":"Lorem Ipsum6", "Descripcio":"Lorem Ipsum", "Lon":16.871931,"Lat":41.175926},{"Nom":"Lorem Ipsum7", "Descripcio":"Lorem Ipsum", "Lon":16.844809,"Lat":41.151096},{"Nom":"Lorem Ipsum8", "Descripcio":"Lorem Ipsum", "Lon":16.855165,"Lat":45}];
    // A l'array data també s'hauria d'afegir un element "desc" per indicar informació del restaurant.

    /*function addPointGeom(data) {

            data.forEach(function(item) { //iterate through array...
                var nom = item.Nom;
                var descripcio = item.Descripcio;
                var longitude = item.Lon,
                    latitude = item.Lat,
                    iconFeature = new ol.Feature({
                        geometry: new ol.geom.Point(ol.proj.transform([longitude, latitude], 'EPSG:4326',
                            'EPSG:3857')),
                      type: 'Point',
                        desc: '<pre> <b>'+nom+' </b> ' + '<br>' + descripcio + '</pre>'}),
                    iconStyle = new ol.style.Style({
                        image: new ol.style.Circle({
                            radius: 5,
                            stroke: new ol.style.Stroke({
                                color: 'blue'
                            }),
                            fill: new ol.style.Fill({
                                color: [57, 228, 193, 0.84]
                            }),
                        })
                    });

                iconFeature.setStyle(iconStyle);

                straitSource.addFeature(iconFeature);
            });
        }// End of function showStraits()*/
    addData();
}