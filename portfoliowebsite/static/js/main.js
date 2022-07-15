$(document).ready(function(){
    const bbtn = document.getElementById('btn2')
    console.log(bbtn)
    bbtn.addEventListener('click', event => {
        $("p").hide();
      });
    });

$(document).ready(function(){

    $(".btn").click(function(){
        $.ajax({
            url: 'demo',
            type: 'get',
            data: {
                button_text: $(this).text()
            },
            succes: function(response) {
                $('.btn').text(response.seconds)
            }

        });
    });
});