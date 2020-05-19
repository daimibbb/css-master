var aCity = [["--请选择--"],
             ["--请选择--", "郑州市", "洛阳市", "开封市", "南阳市", "周口市"], 
             ["--请选择--", "石家庄市", "秦皇岛市", "张家口市"],
             ["--请选择--", "杭州市", "嘉兴市", "温州市"]];
function changeCity() {
    var i, iProvinceIndex;
    iProvinceIndex = document.frm.optProvince.selectedIndex;
    iCityCount = 0;
    while (aCity[iProvinceIndex][iCityCount] != null) {
        iCityCount++;
    }
    document.frm.optCity.length = iCityCount;
    for (i=0; i<iCityCount; i++) {
        document.frm.optCity[i] = new Option(aCity[iProvinceIndex][i]);
    }
}