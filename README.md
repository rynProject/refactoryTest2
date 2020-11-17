# refactoryTest2

pada file App.js terdapat error berupa clientId="" redirectUri="" yang masih kosong sehingga tidak bisa mengakses OAuth dari github,
perubahan yang dilakukan adalah dengan menambahkan clientId, redirectUri, clientSecret.
clientId dan clientSecret didapatkan dari github developer setting bagian OAuth Apps, sedangkan redirectUri di isi dengan callback url pada form OAuth Setting pada github Account

pada file utils.js terdapat error pada let query = `${str}${key}==${params[key]}`; yang menggunakan dua buah = sehingga menyebabkan github login melalui window open tidak dapat
karena menghasilkan response 404 pada page github
kemudian dirubah dengan menghapus satu tanda = menjadi let query = `${str}${key}=${params[key]}`;

pada GithubLogin.js terdapat error pada redirectUri yang masih kosong, kemudian di isi dengan callback url yang didapatkan dari form OAuth Setting pada github account.
fungsi dari redirect url tersebut adalah untuk mengembalikan page ke url awal setelah melakukan login github pada pop up windows yang muncul ketika menekan button sign in using github.

pada line 59 GithubLogin.js terdapat error pada line 59 this.onGetAccessToken(data); parameter yang di pass adalah object yang didapatkan dari pop up windows login github,
sedangkan yang dibutuhkan hanyalah parameter code saja, sehingga code tersebut dirubah menjadi this.onGetAccessToken(data.code);

menambahkan redirect_uri:"http://localhost:3000/" dan state: "name" pada line 72 dan 73

pada line 75 terdapat error CORS yang dikarenakan mengakses API POST milik github menggunakan localhost,
.post(`https://github.com/login/oauth/access_token`, body, options) perubahan yang dilakukan adalah dengan menambahkan CORS anywhere yaitu reverse proxy untuk melakukan bypass terhadap CORS sehingga code menjadi
.post(`https://cors-anywhere.herokuapp.com/https://github.com/login/oauth/access_token`, body, options)

pada API get user pada function onGetProfile(access_token) pada line 82 dibutuhkan acces_token sedangkan yang didapatkan dari .post(`https://cors-anywhere.herokuapp.com/https://github.com/login/oauth/access_token`, body, options)
adalah data berupa object, sedangkan yang dibutuhkan oleh fungsi adalah access_token saja, perubahan yang dilakukan terhadap code adalah
this.onGetProfile(access_token.data.access_token); menambahkan .data.access_token untuk mengakses access_token.

pada props github login component, terdapat property onSuccess yang bertujuan untuk menampilkan nama dari user github.
maka setelah berhasil mengakses onGetProfile(access_token.data.access_token); saya melakukan return menggunakan code this.props.onSuccess(response.data.name);
yang berubah dari sebelumnya this.props.onSuccess(response.data); untuk melakukan pass data name menuju props onSuccess pada file App.js di component github login.
saya mengubah code response.data menjadi response.data.name karena ReactPropt yang di butuhkan untuk set state pada App.js hanyalah data.name saja, sedangkan code sebelumnya melakukan pass berbentuk object.
