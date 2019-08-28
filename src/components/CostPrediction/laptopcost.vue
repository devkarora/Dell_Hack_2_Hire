<template>   
<v-layout row wrap>    
     <div class="text-xs-center">
        <v-dialog v-model="dialog" hide-overlay persistent width="300">
            <v-card color="primary" dark>
                <v-card-text>
                    Placing Order.....
                    <v-progress-linear indeterminate color="white" class="mb-0"></v-progress-linear>
                </v-card-text>
            </v-card>
        </v-dialog>
    </div>
    <alert-component v-if="error" :text="error.message" :color="'error'"></alert-component>
    <alert-component v-if="success" :text="success.message" :color="'success'"></alert-component>
    <v-flex xs12>
        <v-form ref="form">
            <v-layout row wrap>
                <v-flex xs12 class="mb-4">
                    <h1 class="display-1 font-weight-light text-xs-center">
                        <v-icon large color="purple">laptop</v-icon>
                        Cost Prediction for Laptop
                    </h1>
                </v-flex>
                <v-flex xs12>
                </v-flex>
                <v-flex xs12 sm3 class="px-1">
                    <v-select v-model="processor" :items="processors" :rules="[v => !!v || 'Item is required']" label="Processor" required></v-select>
                </v-flex>
                <v-flex xs12 sm3 class="px-1">
                    <v-select v-model="ram" :items="rams" :rules="[v => !!v || 'Item is required']" label="RAM" required></v-select>
                </v-flex>
                <v-flex xs12 sm3 class="px-1">
                    <v-select v-model="hdd" :items="hdds" :rules="[v => !!v || 'Item is required']" label="HDD" required></v-select>
                </v-flex>
                <v-flex xs12 sm3 class="px-1">
                    <v-select v-model="gc" :items="gcs" :rules="[v => !!v || 'Item is required']" label="Graphics Card" required></v-select>
                </v-flex>
                <v-flex xs12 sm3 class="px-1">
                    <v-select v-model="mouse" :items="mouses" :rules="[v => !!v || 'Item is required']" label="Touch Pad" required></v-select>
                </v-flex>
                <v-flex xs12 sm3 class="px-1">
                    <v-select v-model="screen" :items="screens" :rules="[v => !!v || 'Item is required']" label="Screen" required></v-select>
                </v-flex>
                <v-flex xs12 sm3 class="px-1">
                    <v-select v-model="keyboard" :items="keyboards" :rules="[v => !!v || 'Item is required']" label="Keyboard" required></v-select>
                </v-flex>
                <v-flex xs13 class="text-xs-center">
                    <v-btn large round class="accent" @click="pred">
                        <v-icon left>fas fa-chart-line</v-icon>
                        Predict
                    </v-btn>
                </v-flex>
            </v-layout>
        </v-form>
    </v-flex>
    <!-- <v-flex xs12 v-if="predicted">
        <v-layout row wrap>
            <v-flex sm6 xs12 class="text-xs-center">
                <v-icon color="grey" size="70">laptop</v-icon>
                <h1 class="success--text font-weight-light">Great,We have a laptop !</h1>
                <h1>Cost - {{this.cost}} $</h1>
                <v-layout row wrap>
                    <v-flex xs10>
                        <v-progress-linear rounded v-model="reliability" color="indigo" height="10"></v-progress-linear>
                    </v-flex>
                    <v-flex xs2>40 %</v-flex>
                    <v-flex xs10>
                        <v-progress-linear rounded v-model="reliability" color="yellow" height="10"></v-progress-linear>
                    </v-flex>
                    <v-flex xs2>40 %</v-flex>
                    <v-flex xs6 class="text-xs-center">
                        <v-icon color="indigo">fiber_manual_record</v-icon>
                        Supplier Reliability
                    </v-flex>
                    <v-flex xs6 class="text-xs-center">
                        <v-icon color="yellow">fiber_manual_record</v-icon>
                        Component Performance
                    </v-flex>
                </v-layout>
            </v-flex>
            <v-flex sm6 xs12 class="text-xs-center ">
                <v-layout row wrap class="py-4">
                    <v-flex xs4 sm4 class="text-sm-left text-xs-center px-4">
                        <span class="accent--text" style="font-size:18px">Component</span>
                    </v-flex>
                    <v-flex xs8 sm8 class="text-sm-left text-xs-center">
                        <v-layout row wrap>
                            <v-flex xs6 sm6 class="text-xs-center">
                                <span style="font-size:18px" class="accent--text">Supplier</span>
                            </v-flex>
                            <v-flex xs6 sm6 class="text-xs-center">
                                <span style="font-size:18px" class="accent--text">Cost $</span>
                            </v-flex>
                        </v-layout>
                    </v-flex>

                    <v-flex xs4 sm4 class="text-sm-left text-xs-center px-4">
                        <span class="info--text" style="font-size:18px">Processor :</span>
                    </v-flex>
                    <v-flex xs8 sm8 class="text-sm-left text-xs-center">
                        <v-layout row wrap>
                            <v-flex xs6 sm6 class="text-xs-center">
                                <span style="font-size:18px">{{this.info.processor.vendor}}</span>
                            </v-flex>
                            <v-flex xs6 sm6 class="text-xs-center">
                                <span style="font-size:18px">{{this.info.processor.cost}} $</span>
                            </v-flex>
                        </v-layout>
                    </v-flex>

                    <v-flex xs4 sm4 class="text-sm-left text-xs-center px-4">
                        <span class="info--text" style="font-size:18px">RAM :</span>
                    </v-flex>
                    <v-flex xs8 sm8 class="text-sm-left text-xs-center">
                        <v-layout row wrap>
                            <v-flex xs6 sm6 class="text-xs-center">
                                <span style="font-size:18px">{{this.info.ram.vendor}}</span>
                            </v-flex>
                            <v-flex xs6 sm6 class="text-xs-center">
                                <span style="font-size:18px">{{this.info.ram.cost}} $</span>
                            </v-flex>
                        </v-layout>
                    </v-flex>

                    <v-flex xs4 sm4 class="text-sm-left text-xs-center px-4">
                        <span class="info--text" style="font-size:18px">Hardisk :</span>
                    </v-flex>
                    <v-flex xs8 sm8 class="text-sm-left text-xs-center">
                        <v-layout row wrap>
                            <v-flex xs6 sm6 class="text-xs-center">
                                <span style="font-size:18px">{{this.info.hdd.vendor}}</span>
                            </v-flex>
                            <v-flex xs6 sm6 class="text-xs-center">
                                <span style="font-size:18px">{{this.info.hdd.cost}} $</span>
                            </v-flex>
                        </v-layout>
                    </v-flex>

                    <v-flex xs4 sm4 class="text-sm-left text-xs-center px-4">
                        <span class="info--text" style="font-size:18px">Screen :</span>
                    </v-flex>
                    <v-flex xs8 sm8 class="text-sm-left text-xs-center">
                        <v-layout row wrap>
                            <v-flex xs6 sm6 class="text-xs-center">
                                <span style="font-size:18px">{{this.info.screen.vendor}}</span>
                            </v-flex>
                            <v-flex xs6 sm6 class="text-xs-center">
                                <span style="font-size:18px">{{this.info.screen.cost}} $</span>
                            </v-flex>
                        </v-layout>
                    </v-flex>

                    <v-flex xs4 sm4 class="text-sm-left text-xs-center px-4">
                        <span class="info--text" style="font-size:18px">Graphics Card :</span>
                    </v-flex>
                    <v-flex xs8 sm8 class="text-sm-left text-xs-center">
                        <v-layout row wrap>
                            <v-flex xs6 sm6 class="text-xs-center">
                                <span style="font-size:18px">{{this.info.graphicscard.vendor}}</span>
                            </v-flex>
                            <v-flex xs6 sm6 class="text-xs-center">
                                <span style="font-size:18px">{{this.info.graphicscard.cost}} $</span>
                            </v-flex>
                        </v-layout>
                    </v-flex>

                    <v-flex xs4 sm4 class="text-sm-left text-xs-center px-4">
                        <span class="info--text" style="font-size:18px">Mouse :</span>
                    </v-flex>
                    <v-flex xs8 sm8 class="text-sm-left text-xs-center">
                        <v-layout row wrap>
                            <v-flex xs6 sm6 class="text-xs-center">
                                <span style="font-size:18px">{{this.info.mouse.vendor}}</span>
                            </v-flex>
                            <v-flex xs6 sm6 class="text-xs-center">
                                <span style="font-size:18px">{{this.info.mouse.cost}} $</span>
                            </v-flex>
                        </v-layout>
                    </v-flex>

                    <v-flex xs4 sm4 class="text-sm-left text-xs-center px-4">
                        <span class="info--text" style="font-size:18px">Keyboard :</span>
                    </v-flex>
                    <v-flex xs8 sm8 class="text-sm-left text-xs-center">
                        <v-layout row wrap>
                            <v-flex xs6 sm6 class="text-xs-center">
                                <span style="font-size:18px">{{this.info.keyboard.vendor}}</span>
                            </v-flex>
                            <v-flex xs6 sm6 class="text-xs-center">
                                <span style="font-size:18px">{{this.info.keyboard.cost}} $</span>
                            </v-flex>
                        </v-layout>
                    </v-flex>
                </v-layout>
            </v-flex>
        </v-layout>
    </v-flex> -->
    <v-flex xs12 v-if="predicted">
                <v-layout row wrap>
                    <v-flex sm4 xs12 class="text-xs-center">
                        <v-icon color="grey" size="70">laptop</v-icon>                        
                        <h1 class="success--text font-weight-light">Great,We have a laptop !</h1>
                        <h1>Cost - {{this.cost}} $ <v-icon large color="success">fas fa-smile</v-icon>
                        </h1>
                        <v-layout row wrap>
                            <v-flex xs10>
                                <v-progress-linear rounded v-model="reliability" color="indigo" height="10"></v-progress-linear>
                            </v-flex>
                            <v-flex xs2>{{this.reliability}} %</v-flex>
                            <v-flex xs10>
                                <v-progress-linear rounded v-model="performance" color="yellow" height="10"></v-progress-linear>
                            </v-flex>
                            <v-flex xs2>{{this.performance}} %</v-flex>
                            <v-flex xs6 class="text-xs-center">
                                <v-icon color="indigo">fiber_manual_record</v-icon>Supplier Reliability
                            </v-flex>
                            <v-flex xs6 class="text-xs-center">
                                <v-icon color="yellow">fiber_manual_record</v-icon>Component Performance
                            </v-flex>
                        </v-layout>
                    </v-flex>
                    <v-flex sm8 xs12 class="text-xs-center">
                        <v-layout row wrap class="py-4">
                            <v-flex xs4 sm4 class="text-sm-left text-xs-center px-4">
                                <span class="accent--text" style="font-size:18px">Component</span>
                            </v-flex>
                            <v-flex xs8 sm8 class="text-sm-left text-xs-center">
                                <v-layout row wrap>
                                    <v-flex xs4 sm4>
                                        <span style="font-size:18px" class="accent--text">Config</span>
                                    </v-flex>
                                    <v-flex xs4 sm4>
                                        <span style="font-size:18px" class="accent--text">Supplier</span>
                                    </v-flex>
                                    <v-flex xs4 sm4>
                                        <span style="font-size:18px" class="accent--text">Cost $</span>
                                    </v-flex>
                                </v-layout>                                
                            </v-flex>


                            <v-flex xs4 sm4 class="text-sm-left text-xs-center px-4">
                                <span class="info--text" style="font-size:18px">Processor :</span>
                            </v-flex>
                            <v-flex xs8 sm8 class="text-sm-left text-xs-center">
                                <v-layout row wrap>
                                    <v-flex xs4 sm4>
                                        <span style="font-size:18px">{{this.pp.processor}} - {{this.info.processor.besta}},{{this.info.processor.bestb}},{{this.info.processor.bestc}}</span>                                        
                                    </v-flex>
                                    <v-flex xs4 sm4>
                                        <span style="font-size:18px">{{this.info.processor.vendor}}</span>
                                    </v-flex>
                                    <v-flex xs4 sm4>
                                        <span style="font-size:18px">{{this.info.processor.cost}} $</span>
                                    </v-flex>
                                </v-layout>                                
                            </v-flex>

                            <v-flex xs4 sm4 class="text-sm-left text-xs-center px-4">
                                <span class="info--text" style="font-size:18px">RAM :</span>
                            </v-flex>
                            <v-flex xs8 sm8 class="text-sm-left text-xs-center">
                                <v-layout row wrap>
                                    <v-flex xs4 sm4>
                                        <span style="font-size:18px">{{this.pp.ram}} - {{this.info.ram.besta}},{{this.info.ram.bestb}},{{this.info.ram.bestc}}</span>
                                    </v-flex>
                                    <v-flex xs4 sm4>
                                        <span style="font-size:18px">{{this.info.ram.vendor}}</span>
                                    </v-flex>
                                    <v-flex xs4 sm4>
                                        <span style="font-size:18px">{{this.info.ram.cost}} $</span>
                                    </v-flex>
                                </v-layout>                                
                            </v-flex>

                            <v-flex xs4 sm4 class="text-sm-left text-xs-center px-4">
                                <span class="info--text" style="font-size:18px">Hardisk :</span>
                            </v-flex>
                            <v-flex xs8 sm8 class="text-sm-left text-xs-center">
                                <v-layout row wrap>
                                    <v-flex xs4 sm4>
                                        <span style="font-size:18px">{{this.pp.hdd}} - {{this.info.hdd.besta}},{{this.info.hdd.bestb}},{{this.info.hdd.bestc}}</span>
                                    </v-flex>
                                    <v-flex xs4 sm4>
                                        <span style="font-size:18px">{{this.info.hdd.vendor}}</span>
                                    </v-flex>
                                    <v-flex xs4 sm4>
                                        <span style="font-size:18px">{{this.info.hdd.cost}} $</span>
                                    </v-flex>
                                </v-layout>                                
                            </v-flex>

                            <v-flex xs4 sm4 class="text-sm-left text-xs-center px-4">
                                <span class="info--text" style="font-size:18px">Screen :</span>
                            </v-flex>
                            <v-flex xs8 sm8 class="text-sm-left text-xs-center">
                                <v-layout row wrap>
                                    <v-flex xs4 sm4>
                                        <span style="font-size:18px">{{this.pp.screen}}</span>
                                    </v-flex>
                                    <v-flex xs4 sm4>
                                        <span style="font-size:18px">{{this.info.screen.vendor}}</span>
                                    </v-flex>
                                    <v-flex xs4 sm4>
                                        <span style="font-size:18px">{{this.info.screen.cost}} $</span>
                                    </v-flex>
                                </v-layout>                                
                            </v-flex>

                            <v-flex xs4 sm4 class="text-sm-left text-xs-center px-4">
                                <span class="info--text" style="font-size:18px">Graphics Card :</span>
                            </v-flex>
                            <v-flex xs8 sm8 class="text-sm-left text-xs-center">
                                <v-layout row wrap>
                                    <v-flex xs4 sm4>
                                        <span style="font-size:18px">{{this.pp.gc}}</span>
                                    </v-flex>
                                    <v-flex xs4 sm4>
                                        <span style="font-size:18px">{{this.info.graphicscard.vendor}}</span>
                                    </v-flex>
                                    <v-flex xs4 sm4>
                                        <span style="font-size:18px">{{this.info.graphicscard.cost}} $</span>
                                    </v-flex>
                                </v-layout>                                
                            </v-flex>
                            
                            <v-flex xs4 sm4 class="text-sm-left text-xs-center px-4">
                                <span class="info--text" style="font-size:18px">Mouse :</span>
                            </v-flex>
                            <v-flex xs8 sm8 class="text-sm-left text-xs-center">
                                <v-layout row wrap>
                                    <v-flex xs4 sm4>
                                        <span style="font-size:18px">{{this.pp.mouse}}</span>
                                    </v-flex>
                                    <v-flex xs4 sm4>
                                        <span style="font-size:18px">{{this.info.mouse.vendor}}</span>
                                    </v-flex>
                                    <v-flex xs4 sm4>
                                        <span style="font-size:18px">{{this.info.mouse.cost}} $</span>
                                    </v-flex>
                                </v-layout>                                
                            </v-flex>

                            <v-flex xs4 sm4 class="text-sm-left text-xs-center px-4">
                                <span class="info--text" style="font-size:18px">Keyboard :</span>
                            </v-flex>
                            <v-flex xs8 sm8 class="text-sm-left text-xs-center">
                                <v-layout row wrap>
                                    <v-flex xs4 sm4>
                                        <span style="font-size:18px">{{this.pp.keyboard}}</span>
                                    </v-flex>
                                    <v-flex xs4 sm4>
                                        <span style="font-size:18px">{{this.info.keyboard.vendor}}</span>
                                    </v-flex>
                                    <v-flex xs4 sm4>
                                        <span style="font-size:18px">{{this.info.keyboard.cost}} $</span>
                                    </v-flex>
                                </v-layout>                                
                            </v-flex>
                        </v-layout>
                    </v-flex>
                </v-layout>
            </v-flex>
    <v-flex xs12 class="text-xs-center text-sm-center py-4" v-if="predicted">
        <v-btn color="error" @click="reset()" round>Reset</v-btn>        
        <v-btn color="info" @click="placeorder()" round>Place Order</v-btn>        
    </v-flex>    
</v-layout>
</template>

<script>
import axios from "axios"
export default {
    data() {
        return {
            reliability: 0,
            performance: 0,
            processor: '',
            ram: '',
            hdd: '',
            gc: '',
            mouse: '',
            screen: '',
            keyboard: '',
            mouse: '',
            screen: '',
            keyboard: '',
            predicted: false,
            processors: ['i3', 'i5', 'i7', 'i9'],
            rams: ['1 GB', '2 GB', '4 GB', '8 GB', ],
            hdds: ['500 GB', '1 TB', '2 TB'],
            gcs: ['1 GB', '2 GB', '4 GB'],
            mouses: ['Buttonless', 'Traditional'],
            keyboards: ['Simple', 'Soft Touch', 'Backlit'],
            screens: ['23 inch', '24 inch', '27 inch', ],
            cost: 0,
            info: '',
            bottomNav: 3,
            pp:''
        }
    },
    created() {
        this.reset()
        this.predicted = false
    },
    methods: {
        pred() {
            var payload = {
                processor: this.processor,
                ram: this.ram,
                hdd: this.hdd,
                gc: this.gc,
                mouse: this.mouse,
                screen: this.screen,
                keyboard: this.keyboard
            }
            this.pp=payload
            // console.log(payload)            
            var connectionlink = "http://127.0.0.1:5000/getcostoflaptop";
            var config = {
                headers: {
                    "Content-Type": "multipart/form-data",
                    "Access-Control-Allow-Origin": "*"
                }
            };
            axios
                .post(connectionlink, payload, config)
                .then(response => {
                    console.log(response.data)
                    this.info = response.data.data[0]
                    this.cost = response.data.data[1].cost
                    this.reliability=response.data.data[2].supplierreliability;
                    this.performance=response.data.data[3].componenetperformance;
                    this.predicted = true
                })
                .catch(err => {
                    console.log(err);
                });
        },
        reset() {
            this.$refs.form.reset()
            this.$refs.form.resetValidation()
            this.predicted=false
        },
        placeorder(){
            var payload = {
                processor: this.processor,
                ram: this.ram,
                hdd: this.hdd,
                gc: this.gc,
                mouse: this.mouse,
                screen: this.screen,
                keyboard: this.keyboard,
                cost:this.cost
            }
            this.$store.dispatch('placeorder',payload)
            this.reset()
        }
    },
    computed: {
        loading() {
            return this.$store.getters.loading;
        },
        success() {
            return this.$store.getters.success;
        },
        error() {
            return this.$store.getters.error;
        },
    },
    watch: {
        error(err) {
            if (!!err) {
                setTimeout(() => this.$store.dispatch("clearError"), 3000);
            }
        },
        success(con) {
            if (!!con) {
                setTimeout(() => this.$store.dispatch("clearSuccess"), 2000);
            }
        }
    }
}
</script>

<style scoped>

</style>
