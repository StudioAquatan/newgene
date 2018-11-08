window.onload = function () {
    //地図を初期化
    var map = new Y.Map("map");

    //コントロールの追加
    map.addControl(new Y.LayerSetControl());
    map.addControl(new Y.ZoomControl());

    //地図を表示
    map.drawMap(new Y.LatLng(35.680840, 139.767009), 16, Y.LayerSetId.NORMAL);
}