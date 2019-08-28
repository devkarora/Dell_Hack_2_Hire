<template>
<v-layout row wrap>
    <div class="text-xs-center">
        <v-dialog v-model="dialog" hide-overlay persistent width="300">
            <v-card color="primary" dark>
                <v-card-text>
                    Predicting.....
                    <v-progress-linear indeterminate color="white" class="mb-0"></v-progress-linear>
                </v-card-text>
            </v-card>
        </v-dialog>
    </div>
    <alert-component v-if="error" :text="error.message" :color="'error'"></alert-component>
    <alert-component v-if="success" :text="success.message" :color="'success'"></alert-component>
    <v-flex xs12>
        <v-layout row wrap>
            <v-flex xs12 class="text-xs-center mb-5">
                <h1 class="display-1 font-weight-regular">
                    <v-icon class="mr-2" color="green" size="35">fas fa-sliders-h</v-icon>Cost to Configuration
                </h1>
                <span class="text-xs-center" style="font-size:18px;">In this we need to input the cost of the laptop to get the most suitable configurtion with supplier's information.</span>
            </v-flex>
            <v-flex xs12 sm7>
                <v-slider class="py-2" v-model="slider" :readonly="read" thumb-label="always" min="500" label="Cost ?" max="2000"></v-slider>
            </v-flex>
            <v-flex xs12 sm3 class="text-xs-center text-sm-center px-3">
                <v-select v-model="type" :items="types" label="Type" required></v-select>
            </v-flex>
            <v-flex xs12 sm2 class="text-xs-center">
                <v-btn large round class="accent" @click="pred">
                    <v-icon left>fas fa-chart-line</v-icon>Predict
                </v-btn>
            </v-flex>
            <v-flex xs12 v-if="predicted">
                <v-layout row wrap>
                    <v-flex sm4 xs12 class="text-xs-center">
                        <v-icon color="grey" size="70" v-if="this.type=='Laptop'">laptop</v-icon>
                        <v-icon color="grey" size="60" v-if="this.type=='Desktop'">fas fa-desktop</v-icon>
                        <h1 class="success--text font-weight-light">Great,We have a laptop !</h1>
                        <h1>Remaining money - {{this.cost}} $ <v-icon large color="success">fas fa-smile</v-icon>
                        </h1>
                        <v-layout row wrap>
                            <v-flex xs10>
                                <v-progress-linear rounded v-model="performance" color="indigo" height="10"></v-progress-linear>
                            </v-flex>
                            <v-flex xs2>{{this.performance}} %</v-flex>
                            <v-flex xs10>
                                <v-progress-linear rounded v-model="reliability" color="yellow" height="10"></v-progress-linear>
                            </v-flex>
                            <v-flex xs2>{{this.reliability}} %</v-flex>
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
                                        <span style="font-size:18px">{{this.info.processor.part}} - {{this.info.processor.costa}},{{this.info.processor.costb}},{{this.info.processor.costc}}</span>
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
                                        <span style="font-size:18px">{{this.info.ram.part}} - {{this.info.ram.costa}},{{this.info.ram.costb}},{{this.info.ram.costc}}</span>
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
                                        <span style="font-size:18px">{{this.info.hdd.part}} - {{this.info.hdd.costa}},{{this.info.hdd.costb}},{{this.info.hdd.costc}}</span>
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
                                        <span style="font-size:18px">{{this.info.screen.part}}</span>
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
                                        <span style="font-size:18px">{{this.info.graphicscard.part}}</span>
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
                                        <span style="font-size:18px">{{this.info.mouse.part}}</span>
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
                                        <span style="font-size:18px">{{this.info.keyboard.part}}</span>
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
                    <v-flex xs12 class="text-xs-center text-sm-center py-4" v-if="predicted">
                        <v-btn color="error" @click="reset()" round>Reset</v-btn>
                        <v-btn color="info" @click="placeorder()" round>Place Order</v-btn>
                    </v-flex>
                </v-layout>
            </v-flex>
        </v-layout>
    </v-flex>
</v-layout>
</template>

<script>
import axios from "axios";
export default {
    data() {
        return {
            reliability: 0,
            performance: 0,
            slider: 500,
            read: false,
            predicted: false,
            types: ["Laptop", "Desktop"],
            dialog: false,
            cost: 0,
            info: '',
            type: ''
        };
    },
    created() {
        (this.slider = 500), (this.read = false), (this.predicted = false);
    },
    methods: {
        pred() {
            this.dialog = true
            var payload = {
                givenmoney: this.slider,
                // type: this.type
            };
            //http:127.0.0.1:5000/request
            if (this.type == 'Desktop') {
                var connectionlink = "http://127.0.0.1:5000/getconfig";
                var config = {
                    headers: {
                        "Content-Type": "multipart/form-data",
                        "Access-Control-Allow-Origin": "*"
                    }
                };
            } else {
                var connectionlink = "http://127.0.0.1:5000/getconfiglaptop";
                var config = {
                    headers: {
                        "Content-Type": "multipart/form-data",
                        "Access-Control-Allow-Origin": "*"
                    }
                };
            }
            axios
                .post(connectionlink, payload, config)
                .then(response => {
                    console.log(response.data)
                    this.info = response.data.data[0];
                    this.cost = response.data.data[1].cost;
                    this.reliability = response.data.data[2].supplierreliability;
                    this.performance = response.data.data[3].componenetperformance;
                    this.predicted = true
                    this.read = true
                    this.dialog = false
                })
                .catch(err => {
                    console.log(err);
                });
        },
        reset() {
            (this.slider = 500), (this.read = false), (this.predicted = false);
            this.type=''
        },
        placeorder(){
            var payload = {
                processor: this.info.processor.part,
                ram: this.info.ram.part,
                hdd: this.info.hdd.part,
                gc: this.info.graphicscard.part,
                mouse: this.info.mouse.part,
                screen: this.info.screen.part,
                keyboard: this.info.keyboard.part,
                cost:this.cost+this.slider
            }
            console.log(this.payload)
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
};
</script>
