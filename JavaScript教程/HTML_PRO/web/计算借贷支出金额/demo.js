function calculate() {
    // 贷款总额
    // 把年利率从百分比换成十进制，转换成月利率
    // 还款月数
    // 获取文本框的值
    var principal = document.loandata.principal.value;
    var interest = document.loandata.interest.value/100/12;
    var payment = document.loandata.years.value*12;
    // 计算月支付额
    var x = Math.pow(1+interest, payment);
    var monthly = (principal*x*interest)/(x-1);
    // 检查结果是否是无穷大的数
    if ( !isNaN(monthly) && (monthly!=Number.POSITIVE_INFINITY) && (monthly!=Number.NEGATIVE_INFINITY)) {
        document.loandata.payment.value = round(monthly);
        document.loandata.total.value = round(monthly*payment);
        document.loandata.totalinterest.value = round(monthly*payment-principal);
    } else {
        document.loandata.payment.value = "";
        document.loandata.total.value = "";
        document.loandata.totalinterest.value = "";
    }
}
function round(x) {
    return Math.round(x*100)/100;
}