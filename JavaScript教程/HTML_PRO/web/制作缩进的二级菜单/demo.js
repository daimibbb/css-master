function change() {
    var secondDiv = this.parentNode.getElementsByTagName("ul")[0];
    if (secondDiv.className === "myHide") {
        secondDiv.className = "myShow";
    } else {
        secondDiv.className = "myHide";
    }
}
window.onload = function () {
    var listUL = document.getElementById("listUL");
    var allLi = listUL.childNodes;
    var item;
    for (var i=0; i<allLi.length; i++) {
        if (allLi[i].tagName==="li") {
            item = allLi[i].firstChild;
            item.onclick = change;
        }
    }
};

// parentNode：返回指定结点的父节点
// getElementsByTagName方法：返回带有指定标签名的对象的集合
// window.onload：用于在网页加载完毕后立刻执行的操作
// childNodes：返回指定结点的子节点
// tagName：获取元素的标签名