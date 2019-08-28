<template>
<v-layout row>
    <alert-component v-if="error" :text="error.message" :color="'error'"></alert-component>
    <alert-component v-if="success" :text="success.message" :color="'success'"></alert-component>
    <v-dialog v-model="laptopdialog" max-width="500px">       
        <v-card>         
            <v-card-text>
                <v-container grid-list-md>
                    <v-layout wrap>
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-regulat info--text">Processor : </h3>
                        </v-flex>
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-light">{{this.disp.processor.conf}}</h3>
                        </v-flex>                       
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-light">{{this.disp.processor.vendor}}</h3>
                        </v-flex>                       
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-regulat info--text">RAM : </h3>
                        </v-flex>
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-light">{{this.disp.ram.conf}}</h3>
                        </v-flex>                       
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-light">{{this.disp.ram.vendor}}</h3>
                        </v-flex>                       
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-regulat info--text">Screen : </h3>
                        </v-flex>
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-light">{{this.disp.screen.conf}}</h3>
                        </v-flex>                       
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-light">{{this.disp.screen.vendor}}</h3>
                        </v-flex>
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-regulat info--text">Mouse : </h3>
                        </v-flex>
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-light">{{this.disp.mouse.conf}}</h3>
                        </v-flex>                       
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-light">{{this.disp.mouse.vendor}}</h3>
                        </v-flex>
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-regulat info--text">Keyboard : </h3>
                        </v-flex>
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-light">{{this.disp.keyboard.conf}}</h3>
                        </v-flex>                       
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-light">{{this.disp.keyboard.vendor}}</h3>
                        </v-flex>                                             
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-regulat info--text">Graphics Card : </h3>
                        </v-flex>
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-light">{{this.disp.gc.conf}}</h3>
                        </v-flex>                       
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-light">{{this.disp.gc.vendor}}</h3>
                        </v-flex>                                                             
                    </v-layout>
                </v-container>                
            </v-card-text>           
        </v-card>
    </v-dialog>
    <v-dialog v-model="laptopdialog" max-width="500px">       
        <v-card>            
            <v-card-text>
                <v-container grid-list-md>
                    <v-layout wrap>
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-regulat info--text">Processor : </h3>
                        </v-flex>
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-light">{{this.disp.processor.conf}}</h3>
                        </v-flex>                       
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-light">{{this.disp.processor.vendor}}</h3>
                        </v-flex>                       
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-regulat info--text">RAM : </h3>
                        </v-flex>
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-light">{{this.disp.ram.conf}}</h3>
                        </v-flex>                       
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-light">{{this.disp.ram.vendor}}</h3>
                        </v-flex>                       
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-regulat info--text">Screen : </h3>
                        </v-flex>
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-light">{{this.disp.screen.conf}}</h3>
                        </v-flex>                       
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-light">{{this.disp.screen.vendor}}</h3>
                        </v-flex>
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-regulat info--text">Mouse : </h3>
                        </v-flex>
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-light">{{this.disp.mouse.conf}}</h3>
                        </v-flex>                       
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-light">{{this.disp.mouse.vendor}}</h3>
                        </v-flex>
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-regulat info--text">Keyboard : </h3>
                        </v-flex>
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-light">{{this.disp.keyboard.conf}}</h3>
                        </v-flex>                       
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-light">{{this.disp.keyboard.vendor}}</h3>
                        </v-flex>                                             
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-regulat info--text">Graphics Card : </h3>
                        </v-flex>
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-light">{{this.disp.gc.conf}}</h3>
                        </v-flex>                       
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-light">{{this.disp.gc.vendor}}</h3>
                        </v-flex>
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-regulat info--text">HDD : </h3>
                        </v-flex>
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-light">{{this.disp.hdd.conf}}</h3>
                        </v-flex>                       
                        <v-flex xs4 sm4 class="text-xs-center">
                            <h3 class="font-weight-light">{{this.disp.hdd.vendor}}</h3>
                        </v-flex>
                    </v-layout>
                </v-container>                
            </v-card-text>           
        </v-card>
    </v-dialog>
    <v-flex xs12>
        <v-layout row wrap>
            <v-flex x12>
                <h1 style="text-align:center;" class="font-weight-regular">
                    <v-icon color="indigo" size="35" class="mr-2">dashboard</v-icon>Dashboard
                </h1>
                <v-progress-linear v-if="loading" class="mt-0" height="3" color="accent" :indeterminate="loading"></v-progress-linear>
            </v-flex>
            <v-flex xs12 class="text-xs-center">
                <span>Dashboard gives the basic overiew of the entire system,from graphical analysis of component suppliers to order summary.</span>
            </v-flex>
            <v-flex xs12 class="py-3">
                <v-layout row wrap>
                    <v-flex xs12 sm4 class="text-xs-center">
                        <h1 class="font-weight-regular py-2 info--text">Quick Select</h1>
                    </v-flex>
                    <v-flex xs12 sm6 class="text-xs-center">
                        <v-select v-model="type" class="px-5" :items="typeofc" label="Laptop / Desktop" required></v-select>
                    </v-flex>
                </v-layout>
            </v-flex>
            <v-flex xs12>
                <v-layout row wrap>
                    <v-flex xs12 v-if="this.type=='Laptop'">
                        <v-layout row wrap>
                            <v-flex xs12 sm4 class="px-2 text-xs-center py-1" :key="item.key" v-for="item in quicklaptop">
                                <v-card color="blue lighten-5">
                                    <v-card-text>
                                        <v-avatar size="100" color="primary">
                                            <v-icon color="white" size="50">laptop</v-icon>
                                        </v-avatar>                                        
                                    </v-card-text>
                                    <v-card-text>
                                        <h1 class="accent--text">{{item.type}} : {{item.cost}}$</h1>
                                        <span>Recommended for - {{item.use}}</span>
                                    </v-card-text>
                                    <v-card-actions >
                                        <v-layout row wrap>
                                            <v-flex xs12 class="text-xs-center">
                                                <v-btn fab  @click="conflaptopdialog(item.type)"><v-icon>fas fa-eye</v-icon></v-btn>
                                            </v-flex>
                                        </v-layout>                                        
                                    </v-card-actions>
                                </v-card>
                            </v-flex>
                        </v-layout>
                    </v-flex>
                    <v-flex xs12 v-else>
                        <v-layout row wrap>
                            <v-flex xs12 sm4 class="px-2 text-xs-center py-1" :key="item.key" v-for="item in quickdesktop">
                                <v-card color="blue lighten-5">
                                    <v-card-text>
                                        <v-avatar size="100" color="primary">
                                            <v-icon color="white" size="40">fas fa-desktop</v-icon>
                                        </v-avatar>
                                        <!-- <v-divider class="mt-2" color="black"></v-divider> -->
                                    </v-card-text>
                                    <v-card-text>
                                        <h1 class="accent--text">{{item.type}} : {{item.cost}}$</h1>
                                        <span>Recommended for - {{item.use}}</span>
                                    </v-card-text>
                                    <v-card-actions >
                                        <v-layout row wrap>
                                            <v-flex xs12 class="text-xs-center">
                                                <v-btn fab  @click="conflaptopdialog(item.type)"><v-icon>fas fa-eye</v-icon></v-btn>
                                            </v-flex>
                                        </v-layout>                                        
                                    </v-card-actions>
                                </v-card>
                            </v-flex>
                        </v-layout>
                    </v-flex>
                </v-layout>
            </v-flex>
            <v-flex xs12 sm6 class="text-xs-center mt-4">
                <h1 class="font-weight-regular info--text text-xs-center">
                    Our Suppliers
                </h1>
                <v-layout row wrap>
                    <v-flex xs12 class="text-xs-center">
                        <canvas id="supplierchart"></canvas>
                    </v-flex>
                </v-layout>
            </v-flex>
            <v-flex sm6 xs12 class="text-xs-center">
                <h1 class="success--text mt-5 font-weight-regular">Prediction says that Samsung will be our best supplier for the upcoming two years</h1>
                <img :src="samsung" alt="Samsung">
            </v-flex>
            <v-flex xs12>
                <h1 style="text-align:center;" class="font-weight-regular py-3 info--text">
                    Most required Component</h1>
            </v-flex>
            <v-flex xs12 class="text-xs-center">
                <v-layout row wrap>
                    <v-flex sm4 xs12>
                        <v-select v-model="component" class="px-5" :items="components" label="Laptop / Desktop" required></v-select>
                        <v-btn @click="graph()" round color="accent">Predict</v-btn>
                        <h2 class="font-weight-regular success--text py-5" v-if="this.component=='RAM'">
                            Prediction says that 4 GB RAM has to bought from the suppliers in coming year(s).
                        </h2>
                        <h2 class="font-weight-regular success--text py-5" v-if="this.component=='Processor'">
                            Prediction says that i9 processor has to bought from the suppliers in coming year(s).
                        </h2>
                        <h2 class="font-weight-regular success--text py-5" v-if="this.component=='Graphics Card'">
                            Prediction says that 4 GB RAM has to bought from the suppliers in coming year(s).
                        </h2>
                        <h2 class="font-weight-regular success--text py-5" v-if="this.component=='Mouse'">
                            Prediction says that 4 GB RAM has to bought from the suppliers in coming year(s).
                        </h2>
                        <h2 class="font-weight-regular success--text py-5" v-if="this.component=='Keyboard'">
                            Prediction says that 4 GB RAM has to bought from the suppliers in coming year(s).
                        </h2>
                        <h2 class="font-weight-regular success--text py-5" v-if="this.component=='Screen'">
                            Prediction says that 4 GB RAM has to bought from the suppliers in coming year(s).
                        </h2>
                        <h2 class="font-weight-regular success--text py-5" v-if="this.component=='Hardisk'">
                            Prediction says that 1 TB Hardisk has to bought from the suppliers in coming year(s).
                        </h2>
                    </v-flex>
                    <v-flex sm8 xs12 v-if="this.component=='RAM'">
                        <canvas id="ramchart"></canvas>
                    </v-flex>
                    <v-flex sm8 xs12 v-if="this.component=='Processor'">
                        <canvas id="processorchart"></canvas>
                    </v-flex>
                    <v-flex sm8 xs12 v-if="this.component=='Hardisk'">
                        <canvas id="hddchart"></canvas>
                    </v-flex>
                </v-layout>
            </v-flex>
        </v-layout>
    </v-flex>
</v-layout>
</template>

<script>
import samsung from '@/assets/samsung.png'
export default {
    data: function () {
        return {
            laptopdialog:false,
            desktopdialog:false,
            samsung: samsung,
            typeofc: ['Laptop', 'Desktop'],
            type: 'Laptop',
            quicklaptop: [{
                    key: 0,
                    type: 'Budget Saver',
                    cost: 365,
                    use: 'Home Use',
                    config: {

                    }
                },
                {
                    key: 1,
                    type: 'Mid - range',
                    cost: 535,
                    use: 'Professional and Office Use',
                    config: {

                    }
                },
                {
                    key: 2,
                    type: 'High - End',
                    cost: 1183,
                    use: 'Gaming',
                    config: {

                    }
                }
            ],
            quickdesktop: [{
                    type: 'Budget Saver',
                    cost: 353,
                    use: 'Home Use',
                    config: {

                    }
                },
                {
                    type: 'Mid - range',
                    cost: 535,
                    use: 'Professional and Office Use',
                    config: {

                    }
                },
                {
                    type: 'High - End',
                    cost: 1138,
                    use: 'Gaming purpose',
                    config: {

                    }
                }
            ],
            component: 'RAM',
            components: ['RAM', 'Processor', 'Hardisk', 'Graphics Card', 'Mouse', 'Keyboard', 'Screen'],
            disp:{
                    'processor': {
                        'conf': 'i3',
                        'vendor': 'Intel'
                    },
                    'ram': {
                        'conf': '1 GB',
                        'vendor': 'Samsung'
                    },                    
                    'screen': {
                        'conf': '23 inch',
                        'vendor': 'Samsung'
                    },
                    'keyboard': {
                        'conf': 'Simple',
                        'vendor': 'Wester Digital'
                    },
                    'hdd': {
                        'conf': '500 GB',
                        'vendor': 'WD Elements'
                    },
                    'mouse': {
                        'conf': '3 Click',
                        'vendor': 'Intel'
                    },
                    'gc':{
                        'conf':'1 GB',
                        'vendor':'Intel'
                    }
                }
            }
    },
    mounted() {
        this.suppliergraph()
        this.ramgraph()
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
        }
    },
    methods: {
        suppliergraph() {
            var q = [{
                x: 2005,
                y: 8.8
            }, {
                x: 2006,
                y: 8.7
            }, {
                x: 2007,
                y: 8.5
            }, {
                x: 2008,
                y: 8.4
            }, {
                x: 2009,
                y: 8.8
            }, {
                x: 2010,
                y: 7.5
            }, {
                x: 2011,
                y: 7.1
            }, {
                x: 2012,
                y: 8.5
            }, {
                x: 2013,
                y: 8.9
            }, {
                x: 2014,
                y: 9.1
            }, {
                x: 2015,
                y: 8.4
            }, {
                x: 2016,
                y: 7.6
            }, {
                x: 2017,
                y: 7.5
            }, {
                x: 2018,
                y: 7.9
            }, {
                x: 2019,
                y: 8.1
            }, {
                x: 2020,
                y: 7.6
            }, ]
            var r = [{
                x: 2005,
                y: 5.6
            }, {
                x: 2006,
                y: 5.7
            }, {
                x: 2007,
                y: 5.3
            }, {
                x: 2008,
                y: 5.7
            }, {
                x: 2009,
                y: 5.8
            }, {
                x: 2010,
                y: 5.9
            }, {
                x: 2011,
                y: 6.5
            }, {
                x: 2012,
                y: 6.1
            }, {
                x: 2013,
                y: 5.5
            }, {
                x: 2014,
                y: 5.4
            }, {
                x: 2015,
                y: 6.5
            }, {
                x: 2016,
                y: 7.1
            }, {
                x: 2017,
                y: 7.3
            }, {
                x: 2018,
                y: 7.4
            }, {
                x: 2019,
                y: 8.2
            }, {
                x: 2020,
                y: 9.1
            }, ]
            var s = [{
                x: 2005,
                y: 6.5
            }, {
                x: 2006,
                y: 8.5
            }, {
                x: 2007,
                y: 8.4
            }, {
                x: 2008,
                y: 8
            }, {
                x: 2009,
                y: 6.5
            }, {
                x: 2010,
                y: 5.9
            }, {
                x: 2011,
                y: 5.4
            }, {
                x: 2012,
                y: 5
            }, {
                x: 2013,
                y: 4.1
            }, {
                x: 2014,
                y: 4.4
            }, {
                x: 2015,
                y: 4.9
            }, {
                x: 2016,
                y: 5.2
            }, {
                x: 2017,
                y: 5.4
            }, {
                x: 2018,
                y: 5.5
            }, {
                x: 2019,
                y: 7.7
            }, {
                x: 2020,
                y: 8.2
            }, ]
            var ctx = document.getElementById("supplierchart")
            var linechart = new Chart(ctx, {
                type: "line",
                data: {
                    datasets: [{
                            label: "Intel",
                            data: q,
                            type: "line",
                            fill: false,
                            pointRadius: 0,
                            borderColor: "#64B5F6"
                        },
                        {
                            label: "Samsung",
                            data: r,
                            type: "line",
                            fill: false,
                            pointRadius: 0,
                            borderColor: "#F57C00"
                        },
                        {
                            label: "Western Digital",
                            data: s,
                            type: "line",
                            fill: false,
                            pointRadius: 0,
                            borderColor: "#37474F"
                        }
                    ]
                },
                options: {
                    scales: {
                        yAxes: [{
                            scaleLabel: {
                                display: true,
                                labelString: "Quantity in 10^4"
                            }
                        }],
                        xAxes: [{
                            type: "linear",
                            position: "bottom",
                            scaleLabel: {
                                display: true,
                                labelString: "Year"
                            }
                        }]
                    },
                    animation: {
                        duration: 5000 // general animation time
                    },
                    responsiveAnimationDuration: 2000
                }
            });
        },
        ramgraph() {
            var a = [{
                x: 2005,
                y: 105
            }, {
                x: 2006,
                y: 108
            }, {
                x: 2007,
                y: 113
            }, {
                x: 2008,
                y: 116
            }, {
                x: 2009,
                y: 121
            }, {
                x: 2010,
                y: 127
            }, {
                x: 2011,
                y: 130
            }, {
                x: 2012,
                y: 131
            }, {
                x: 2013,
                y: 133
            }, {
                x: 2014,
                y: 136
            }, {
                x: 2015,
                y: 132
            }, {
                x: 2016,
                y: 135
            }, {
                x: 2017,
                y: 127
            }, {
                x: 2018,
                y: 120
            }, {
                x: 2019,
                y: 111
            }, {
                x: 2020,
                y: 98
            }, ]
            var b = [{
                x: 2005,
                y: 91
            }, {
                x: 2006,
                y: 100
            }, {
                x: 2007,
                y: 105
            }, {
                x: 2008,
                y: 109
            }, {
                x: 2009,
                y: 113
            }, {
                x: 2010,
                y: 121
            }, {
                x: 2011,
                y: 122
            }, {
                x: 2012,
                y: 126
            }, {
                x: 2013,
                y: 135
            }, {
                x: 2014,
                y: 141
            }, {
                x: 2015,
                y: 151
            }, {
                x: 2016,
                y: 145
            }, {
                x: 2017,
                y: 142
            }, {
                x: 2018,
                y: 141
            }, {
                x: 2019,
                y: 136
            }, {
                x: 2020,
                y: 129
            }, ]
            var c = [{
                x: 2005,
                y: 67
            }, {
                x: 2006,
                y: 71
            }, {
                x: 2007,
                y: 74
            }, {
                x: 2008,
                y: 78
            }, {
                x: 2009,
                y: 75
            }, {
                x: 2010,
                y: 76
            }, {
                x: 2011,
                y: 85
            }, {
                x: 2012,
                y: 83
            }, {
                x: 2013,
                y: 87
            }, {
                x: 2014,
                y: 92
            }, {
                x: 2015,
                y: 110
            }, {
                x: 2016,
                y: 152
            }, {
                x: 2017,
                y: 172
            }, {
                x: 2018,
                y: 173
            }, {
                x: 2019,
                y: 221
            }, {
                x: 2020,
                y: 260
            }, ]
            var d = [{
                x: 2005,
                y: 58
            }, {
                x: 2006,
                y: 65
            }, {
                x: 2007,
                y: 77
            }, {
                x: 2008,
                y: 81
            }, {
                x: 2009,
                y: 99
            }, {
                x: 2010,
                y: 102
            }, {
                x: 2011,
                y: 109
            }, {
                x: 2012,
                y: 116
            }, {
                x: 2013,
                y: 134
            }, {
                x: 2014,
                y: 136
            }, {
                x: 2015,
                y: 142
            }, {
                x: 2016,
                y: 149
            }, {
                x: 2017,
                y: 167
            }, {
                x: 2018,
                y: 180
            }, {
                x: 2019,
                y: 192
            }, {
                x: 2020,
                y: 207
            }, ]
            var ctx = document.getElementById("ramchart")
            var linechart = new Chart(ctx, {
                type: "line",
                data: {
                    datasets: [{
                            label: "1 GB",
                            data: a,
                            type: "line",
                            fill: false,
                            pointRadius: 0,
                            borderColor: "#64B5F6"
                        },
                        {
                            label: "2 GB",
                            data: b,
                            type: "line",
                            fill: false,
                            pointRadius: 0,
                            borderColor: "#F57C00"
                        },
                        {
                            label: "4 GB",
                            data: c,
                            type: "line",
                            fill: false,
                            pointRadius: 0,
                            borderColor: "#37474F"
                        },
                        {
                            label: "8 GB",
                            data: d,
                            type: "line",
                            fill: false,
                            pointRadius: 0,
                            borderColor: "#CDDC39"
                        }
                    ]
                },
                options: {
                    scales: {
                        yAxes: [{
                            scaleLabel: {
                                display: true,
                                labelString: "Quantity in 10^4"
                            }
                        }],
                        xAxes: [{
                            type: "linear",
                            position: "bottom",
                            scaleLabel: {
                                display: true,
                                labelString: "Year"
                            }
                        }]
                    },
                    animation: {
                        duration: 5000 // general animation time
                    },
                    responsiveAnimationDuration: 2000
                }
            });
        },
        processorgraph() {
            var a = [{
                x: 2005,
                y: 23
            }, {
                x: 2006,
                y: 25
            }, {
                x: 2007,
                y: 26
            }, {
                x: 2008,
                y: 24
            }, {
                x: 2009,
                y: 29
            }, {
                x: 2010,
                y: 33
            }, {
                x: 2011,
                y: 35
            }, {
                x: 2012,
                y: 35
            }, {
                x: 2013,
                y: 37
            }, {
                x: 2014,
                y: 37
            }, {
                x: 2015,
                y: 38
            }, {
                x: 2016,
                y: 40
            }, {
                x: 2017,
                y: 40
            }, {
                x: 2018,
                y: 41
            }, {
                x: 2019,
                y: 39
            }, {
                x: 2020,
                y: 38
            }, ]
            var b = [{
                x: 2005,
                y: 20
            }, {
                x: 2006,
                y: 24
            }, {
                x: 2007,
                y: 23
            }, {
                x: 2008,
                y: 26
            }, {
                x: 2009,
                y: 27
            }, {
                x: 2010,
                y: 29
            }, {
                x: 2011,
                y: 30
            }, {
                x: 2012,
                y: 34
            }, {
                x: 2013,
                y: 38
            }, {
                x: 2014,
                y: 41
            }, {
                x: 2015,
                y: 41
            }, {
                x: 2016,
                y: 43
            }, {
                x: 2017,
                y: 44
            }, {
                x: 2018,
                y: 47
            }, {
                x: 2019,
                y: 47
            }, {
                x: 2020,
                y: 48
            }, ]
            var c = [{
                x: 2005,
                y: 0
            }, {
                x: 2006,
                y: 0
            }, {
                x: 2007,
                y: 0
            }, {
                x: 2008,
                y: 0
            }, {
                x: 2009,
                y: 5
            }, {
                x: 2010,
                y: 5.4
            }, {
                x: 2011,
                y: 5.9
            }, {
                x: 2012,
                y: 11
            }, {
                x: 2013,
                y: 19
            }, {
                x: 2014,
                y: 31
            }, {
                x: 2015,
                y: 38
            }, {
                x: 2016,
                y: 41
            }, {
                x: 2017,
                y: 45
            }, {
                x: 2018,
                y: 50
            }, {
                x: 2019,
                y: 55
            }, {
                x: 2020,
                y: 58
            }, ]
            var d = [{
                x: 2005,
                y: 0
            }, {
                x: 2006,
                y: 0
            }, {
                x: 2007,
                y: 0
            }, {
                x: 2008,
                y: 0
            }, {
                x: 2009,
                y: 0
            }, {
                x: 2010,
                y: 4
            }, {
                x: 2011,
                y: 5
            }, {
                x: 2012,
                y: 11
            }, {
                x: 2013,
                y: 17
            }, {
                x: 2014,
                y: 24
            }, {
                x: 2015,
                y: 27
            }, {
                x: 2016,
                y: 37
            }, {
                x: 2017,
                y: 42
            }, {
                x: 2018,
                y: 51
            }, {
                x: 2019,
                y: 61
            }, {
                x: 2020,
                y: 63
            }, ]
            var ctx = document.getElementById("processorchart")
            var linechart = new Chart(ctx, {
                type: "line",
                data: {
                    datasets: [{
                            label: "i3",
                            data: a,
                            type: "line",
                            fill: false,
                            pointRadius: 0,
                            borderColor: "#64B5F6"
                        },
                        {
                            label: "i5",
                            data: b,
                            type: "line",
                            fill: false,
                            pointRadius: 0,
                            borderColor: "#F57C00"
                        },
                        {
                            label: "i7",
                            data: c,
                            type: "line",
                            fill: false,
                            pointRadius: 0,
                            borderColor: "#37474F"
                        },
                        {
                            label: "i9",
                            data: d,
                            type: "line",
                            fill: false,
                            pointRadius: 0,
                            borderColor: "#CDDC39"
                        }
                    ]
                },
                options: {
                    scales: {
                        yAxes: [{
                            scaleLabel: {
                                display: true,
                                labelString: "Quantity in 10^4"
                            }
                        }],
                        xAxes: [{
                            type: "linear",
                            position: "bottom",
                            scaleLabel: {
                                display: true,
                                labelString: "Year"
                            }
                        }]
                    },
                    animation: {
                        duration: 5000 // general animation time
                    },
                    responsiveAnimationDuration: 2000
                }
            });
        },
        hddgraph() {
            var a = [{
                x: 2005,
                y: 23
            }, {
                x: 2006,
                y: 25
            }, {
                x: 2007,
                y: 26
            }, {
                x: 2008,
                y: 26
            }, {
                x: 2009,
                y: 24
            }, {
                x: 2010,
                y: 29
            }, {
                x: 2011,
                y: 33
            }, {
                x: 2012,
                y: 35
            }, {
                x: 2013,
                y: 35
            }, {
                x: 2014,
                y: 37
            }, {
                x: 2015,
                y: 38
            }, {
                x: 2016,
                y: 40
            }, {
                x: 2017,
                y: 40
            }, {
                x: 2018,
                y: 41
            }, {
                x: 2019,
                y: 39
            }, {
                x: 2020,
                y: 38
            }, ]
            var b = [{
                x: 2005,
                y: 20
            }, {
                x: 2006,
                y: 24
            }, {
                x: 2007,
                y: 23
            }, {
                x: 2008,
                y: 26
            }, {
                x: 2009,
                y: 27
            }, {
                x: 2010,
                y: 29
            }, {
                x: 2011,
                y: 30
            }, {
                x: 2012,
                y: 33
            }, {
                x: 2013,
                y: 36
            }, {
                x: 2014,
                y: 38
            }, {
                x: 2015,
                y: 43
            }, {
                x: 2016,
                y: 47
            }, {
                x: 2017,
                y: 48
            }, {
                x: 2018,
                y: 51
            }, {
                x: 2019,
                y: 55
            }, {
                x: 2020,
                y: 58
            }, ]
            var c = [{
                x: 2005,
                y: 12
            }, {
                x: 2006,
                y: 13
            }, {
                x: 2007,
                y: 14
            }, {
                x: 2008,
                y: 17
            }, {
                x: 2009,
                y: 20
            }, {
                x: 2010,
                y: 24
            }, {
                x: 2011,
                y: 27
            }, {
                x: 2012,
                y: 31
            }, {
                x: 2013,
                y: 32
            }, {
                x: 2014,
                y: 35
            }, {
                x: 2015,
                y: 38
            }, {
                x: 2016,
                y: 39
            }, {
                x: 2017,
                y: 44
            }, {
                x: 2018,
                y: 49
            }, {
                x: 2019,
                y: 50
            }, {
                x: 2020,
                y: 53
            }, ]
            var ctx = document.getElementById("hddchart")
            var linechart = new Chart(ctx, {
                type: "line",
                data: {
                    datasets: [{
                            label: "500 GB",
                            data: a,
                            type: "line",
                            fill: false,
                            pointRadius: 0,
                            borderColor: "#64B5F6"
                        },
                        {
                            label: "1 TB",
                            data: b,
                            type: "line",
                            fill: false,
                            pointRadius: 0,
                            borderColor: "#F57C00"
                        },
                        {
                            label: "2 TB",
                            data: c,
                            type: "line",
                            fill: false,
                            pointRadius: 0,
                            borderColor: "#37474F"
                        }
                    ]
                },
                options: {
                    scales: {
                        yAxes: [{
                            scaleLabel: {
                                display: true,
                                labelString: "Quantity in 10^4"
                            }
                        }],
                        xAxes: [{
                            type: "linear",
                            position: "bottom",
                            scaleLabel: {
                                display: true,
                                labelString: "Year"
                            }
                        }]
                    },
                    animation: {
                        duration: 5000 // general animation time
                    },
                    responsiveAnimationDuration: 2000
                }
            });
        },
        graph() {
            if (this.component == 'RAM')
                this.ramgraph()
            else if (this.component == 'Processor')
                this.processorgraph()
            else if (this.component == 'Graphics Card')
                this.gcgraph()
            else if (this.component == 'Mouse')
                this.mousegraph()
            else if (this.component == 'Keyboard')
                this.keygraph()
            else if (this.component == 'Screen')
                this.screengraph()
            else if (this.component == 'Hardisk')
                this.hddgraph()
        },
        conflaptopdialog(val) {            
            if (val == 'Budget Saver') {
                var obj = {
                    'processor': {
                        'conf': 'i3',
                        'vendor': 'Samsung'
                    },
                    'ram': {
                        'conf': '1 GB',
                        'vendor': 'Samsung'
                    },
                    'gc': {
                        'conf': '1 GB',
                        'vendor': 'Western Digital'
                    },
                    'screen': {
                        'conf': '23 inch',
                        'vendor': 'Intel'
                    },
                    'keyboard': {
                        'conf': 'Simple',
                        'vendor': 'Intel'
                    },
                    'hdd': {
                        'conf': '500 GB',
                        'vendor': 'Samsung'
                    },
                    'mouse': {
                        'conf': '3 Click',
                        'vendor': 'Samsung'
                    }
                }
                this.disp = obj                
                this.laptopdialog = true
            }
            else if(val =='Mid - range'){
                var obj = {
                    'processor': {
                        'conf': 'i5',
                        'vendor': 'Intel'
                    },
                    'ram': {
                        'conf': '2 GB',
                        'vendor': 'Samsung'
                    },
                    'gc': {
                        'conf': '2 GB',
                        'vendor': 'Intel'
                    },
                    'screen': {
                        'conf': '24 inch',
                        'vendor': 'Samsung'
                    },
                    'keyboard': {
                        'conf': 'Backlit',
                        'vendor': 'Intel'
                    },
                    'hdd': {
                        'conf': '1 TB',
                        'vendor': 'WD Elements'
                    },
                    'mouse': {
                        'conf': '5 Click',
                        'vendor': 'Intel'
                    }
                }
                this.disp = obj                
                this.laptopdialog = true
            }else{
                var obj = {
                    'processor': {
                        'conf': 'i9',
                        'vendor': 'Intel'
                    },
                    'ram': {
                        'conf': '8 GB',
                        'vendor': 'Samsung'
                    },
                    'gc': {
                        'conf': '4 GB',
                        'vendor': 'WD'
                    },
                    'screen': {
                        'conf': '27 inch',
                        'vendor': 'Samsung'
                    },
                    'keyboard': {
                        'conf': 'Soft Touch',
                        'vendor': 'Intel'
                    },
                    'hdd': {
                        'conf': '2 TB',
                        'vendor': 'Intel'
                    },
                    'mouse': {
                        'conf': '5 Click',
                        'vendor': 'Intel'
                    }
                }
                this.disp = obj                
                this.laptopdialog = true
            }
        },
        confdesktopdialog(val) {            
            if (val == 'Budget Saver') {
                var obj = {
                    'processor': {
                        'conf': 'i3',
                        'vendor': 'Samsung'
                    },
                    'ram': {
                        'conf': '1 GB',
                        'vendor': 'Samsung'
                    },
                    'gc': {
                        'conf': '1 GB',
                        'vendor': 'Western Digital'
                    },
                    'screen': {
                        'conf': '23 inch',
                        'vendor': 'Intel'
                    },
                    'keyboard': {
                        'conf': 'Simple',
                        'vendor': 'Itel'
                    },
                    'hdd': {
                        'conf': '500 GB',
                        'vendor': 'Samsung'
                    },
                    'mouse': {
                        'conf': '3 Click',
                        'vendor': 'Samsung'
                    }
                }
                this.disp = obj                
                this.laptopdialog = true
            }
            else if(val =='Mid - range'){
                var obj = {
                    'processor': {
                        'conf': 'i5',
                        'vendor': 'Intel'
                    },
                    'ram': {
                        'conf': '2 GB',
                        'vendor': 'Samsung'
                    },
                    'gc': {
                        'conf': '2 GB',
                        'vendor': 'Intel'
                    },
                    'screen': {
                        'conf': '24 inch',
                        'vendor': 'Samsung'
                    },
                    'keyboard': {
                        'conf': 'Backlit',
                        'vendor': 'Intel'
                    },
                    'hdd': {
                        'conf': '1 TB',
                        'vendor': 'WD Elements'
                    },
                    'mouse': {
                        'conf': '5 Click',
                        'vendor': 'Intel'
                    }
                }
                this.disp = obj                
                this.laptopdialog = true
            }else{
                var obj = {
                    'processor': {
                        'conf': 'i9',
                        'vendor': 'Intel'
                    },
                    'ram': {
                        'conf': '8 GB',
                        'vendor': 'Samsung'
                    },
                    'gc': {
                        'conf': '4 GB',
                        'vendor': 'WD'
                    },
                    'screen': {
                        'conf': '27 inch',
                        'vendor': 'Samsung'
                    },
                    'keyboard': {
                        'conf': 'Soft Touch',
                        'vendor': 'Intel'
                    },
                    'hdd': {
                        'conf': '2 TB',
                        'vendor': 'Intel'
                    },
                    'mouse': {
                        'conf': '5 Click',
                        'vendor': 'Intel'
                    }
                }
                this.disp = obj                
                this.laptopdialog = true
            }
        }
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
