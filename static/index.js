layui.use(['layer', 'util', 'element'], function () {
    const element = layui.element;
    const layer = layui.layer;
    const util = layui.util;
    const $ = layui.$

    load();

    util.fixbar({
        bar1:true,
        bar2:true,
        css:{right: 30, bottom: 100},
        bgcolor:'#393D45',
        click: function (type) {
            if (type === 'bar1'){
                // 刷新页面
                location.reload()
            }else if (type === 'bar2'){
                layer.msg('两个 bar 都可以设定是否开启')
            }
        }
    });

    // 动态加载
    function load(){
       $.ajax({
           url:"/api/wy",
           type:"GET",
           data:{page:1,limit:30},
           success:function(data){
               const conter = $('#fh5co-board')[0];
               const hts = [];
               // 遍历数据
               for(let i=1; i<=30; i++){

                   // 截取字符串
                   const tem = data['data'][i-1].song_name
                   const tem1 = data['data'][i-1].singer_name
                   const song_name = tem.substring(0,11)
                   const singer_name = tem1.substring(0,4)
                   // hts[i-1] 直接向数组中第一个元素赋值
                   hts[i-1]=$(`
                    <div class="item">
                        <div class="layui-card">
                            <div class="layui-card-header">
                              <b>歌曲：${song_name}--${singer_name}</b>
                               <a class="layui-icon" href="https://music.163.com/#/song?id=${data['data'][i-1].song_id}" target="_blank">&#xe652;</a>
                            </div>
                            <div class="layui-card-body">
                              <p>${data['data'][i-1].comment}</p><br>
                              <p style="text-align: right">热评发表日期: ${data['data'][i-1].comment_date}<i class="layui-icon layui-icon-praise layui-badge layui-bg-blue">${data['data'][i-1].likedCount}</i></p>
                            </div>
                        </div>
                         <div class="layui-card">
                            <div class="layui-card-header">
                                <a href="https://music.163.com/#/user/home?id=${data['data'][i-1].user_id}" 
                             target="_blank"><b>热评出自：${data['data'][i-1].user_name}</b>
                             <img src="${data['data'][i-1].head_link}"></a>
                            </div>
                         </div>
                    </div>
                `)[0];
                }
               // salvattore方法的append_elements方法，将数组追加到div的最后面。
                salvattore.append_elements(conter, hts);
           },
     　　　　　　
           error: function (jqXHR, textStatus, err) {

                    console.log(arguments);
                },

           complete: function (jqXHR, textStatus) {
                    console.log(textStatus);
            },

           statusCode: {
                '403': function (jqXHR, textStatus, err) {
                      console.log(arguments);
                 },

                '400': function (jqXHR, textStatus, err) {
                    console.log(arguments);
                }
            }
       });
    }

});


// 下拉到底部事件
/*
$(window).scroll(function(){
    const scrollh = $(document).height();
    const scrollTop = Math.max(document.documentElement.scrollTop || document.body.scrollTop);
    if((scrollTop + $(window).height()) >= scrollh){
        location.reload()
    }
});
*/
