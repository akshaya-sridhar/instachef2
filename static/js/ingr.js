function ingr()
{
    var selected = new Array();
    var checkbox = document.getElementById('ingr_id');
    var chk = document.getElementsByTagName('input');
    for(i = 0; i< chk.length;i++)
    {
        if(chk[i].checked)
        {
            selected.push(chk[i].value);
        }
    }
}