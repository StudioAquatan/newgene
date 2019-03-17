function load_map(map, lat, lng) {
    //地図を初期化
    var map = new Y.Map(map.toString(10));

    //コントロールの追加
    map.addControl(new Y.LayerSetControl());
    map.addControl(new Y.ZoomControl());

    //地図を表示
    map.drawMap(new Y.LatLng(lat, lng), 16, Y.LayerSetId.NORMAL);

    //マーカーの追加
    var marker = new Y.Marker(new Y.LatLng(lat, lng));
    map.addFeature(marker);
}