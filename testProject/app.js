const express = require('express');
const request = require('request');
const app = express();


app.use(express.static('./'));

app.get('/', function (req, res) {
  res.render('index')

  
  /*
      <script>
        $.ajax({
            method: "GET",
            url: "https://kapi.kakao.com/v1/translation/translate",
            data: {
                urlencode : { query: "apple", src_lang: "en", target_lang : "kr" }
            },
            headers : { Authorization : "KakaoAK 119e4cd6f7423ed520b6969e6e9917ce"}
        })
            .done(function (msg) {
                alert("Data Saved: " + msg);
            });
    </script>
  */
})

app.listen(3000, function () {
    console.log("서버가동")
  })