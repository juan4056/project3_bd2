Vue.options.delimiters = ['{[{', '}]}'];
var v = new Vue({
    el:'#app',
    data:{
        selectedFile: null,
        urlFile : null,
        imagefiles : [],
        totalTweets: 0,
        text:'',
        msg:[],
        spinner : false,
        spinner2 : false,
        temp: ""
    },
    methods: {
        clearSearchField(){
        },
        upselectedFile(event){
            this.selectedFile=event.target.files[0];
            this.urlFile = URL.createObjectURL(this.selectedFile)
            this.temp = "./static/lfw/Aaron_Peirsol/Aaron_Peirsol_0002.jpg"
        },
        async send() {
            this.spinner = true

            const fd = new FormData()
            fd.append('image', this.selectedFile)
            console.log(this.selectedFile)
            
            var url = 'http://127.0.0.1:5000/upload'
            var array = []
            await axios.post(url, fd)
            .then(function(res){
                console.log(res)
                for (var i = 0; i < res.data.result.length; i++){
                    var name_foto = res.data.result[i]
                    var name = name_foto.split("_")
                    var final_name = ""
                    for (var j = 0; j < name.length - 2; j++){
                        final_name = final_name + name[j] + "_"
                    }
                    final_name = final_name + name[name.length - 2]
                    array.push("./static/lfw/" + final_name + "/" + name_foto)
                }
                console.log(this.imagefiles)
            })
            .catch(function(err){
                console.log(err)
            })

            this.imagefiles = array

            this.spinner = false
        },
        async build() {
            this.spinner = true
            
            var url = 'http://127.0.0.1:5000/build'

            await axios.get(url)
            .then(function(res){
                console.log(res)
            })
            .catch(function(err){
                console.log(err)
            })

            this.spinner = false
        },
        async upLoadAll(){
            this.spinner2 = true
            let newtotal = 0
            const fd = new FormData();
            //fd.append('files',this.selectedFile.length,this.selectedFile.length)
            for(i=0;i<this.selectedFile.length;i++){
                fd.append('json'+i,this.selectedFile[i],this.selectedFile[i].name)
            }
            var url='http://127.0.0.1:5000/upload';
            await axios.post(url,fd)
            .then(function(res){
                console.log(res.data)
                console.log(res.data.total)
                this.totalTweets = res.data.total
                newtotal = res.data.total
                console.log(this.totalTweets)
                if(res.data.status==201)
                    console.log("exitos")
                })
            .catch(function(err){
                console.log(err)
            })
            .then(function(){
                console.log("Finish")
            })
            this.spinner2 = false
            this.totalTweets = newtotal
        },
        async search(to_search) {
            console.log("consulta entro a search")
            this.spinner = true
            const path = 'http://localhost:5000/tweets/' + to_search;
            await axios.get(path)
                .then((res) => {
                this.msg = res.data;
                this.msg.sort((a,b) => (a.score < b.score) ? 1 : ((b.score < a.score) ? -1 : 0));
            })
            .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
            });
            this.spinner = false
        }
    },
    computed: {
        nameSelectedFile(){
            var i;
            selectFiles=[]
            for(i=0;i<this.selectedFile.length;i++){
                console.log(this.selectedFile[i].name)
                selectFiles.push(this.selectedFile[i]);
            }
            return selectFiles
        }
    },

});