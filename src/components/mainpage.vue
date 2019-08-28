<template>
<section>
    <alert-component v-if="error" :text="error.message" :color="'error'"></alert-component>
    <alert-component v-if="success" :text="success.message" :color="'success'"></alert-component>
    <v-app light>
        <v-content>
            <section>
                <v-parallax style="background-image:linear-gradient(#0D47A1,#2196F3)" height="400">
                    <v-layout column align-center justify-center class="white--text">
                        <img :src="logo" alt="Dell_logo" height="200">
                        <v-btn round large class="primary mt-4" :href="userstatus">
                            <v-icon size="30" left>fas fa-play-circle</v-icon>
                            Get Started
                        </v-btn>
                    </v-layout>
                </v-parallax>
            </section>

            <section class>
                <br>
                <br>
                <v-layout row wrap class align-center>
                    <v-flex xs12 class="my-2">
                        <div class="text-xs-center">
                            <!-- <v-icon size="100" class="primary--text">fas fa-graduation-cap</v-icon> -->
                            <h1 class="text-xs-center mb-4 font-weight-light" style="font-family:'Monospace'; font-size:30px;">About DELL</h1>
                            <span class="subheading">" THE POWER TO DO MORE "</span>
                        </div>
                    </v-flex>
                    <v-flex xs12>
                        <v-layout row wrap align-center>
                            <v-flex>
                                <v-card class="elevation-0 transparent" flat>
                                    <v-card-title class="layout justify-center">
                                        <h2 class="font-weight-light px-5 text-xs-center" style="text-align: justify;">Dell is a US multinational computer technology company that develops, sells, repairs, and supports computers and related products and services. Named after its founder, Michael Dell, the company is one of the largest technological corporations in the world, employing more than 145,000 people in the U.S. and around the world (Annual report 2018).</h2>
                                    </v-card-title>
                                </v-card>
                            </v-flex>
                        </v-layout>
                    </v-flex>
                </v-layout>
                <br>
                <br>
            </section>

            <section>
                <v-layout row wrap class="my-3" align-center>
                    <!-- <v-flex xs12 class="">
                        <div class="text-xs-center">
                            <h1 class="text-xs-center mb-4 font-weight-light" style="font-family:'Monospace'; font-size:30px;">Getting Started</h1>
                        </div>
                    </v-flex> -->
                    <v-flex xs12 class="text-xs-center">
                        <h1 class="display-1">Bill Of Material - Cost Prediction</h1>
                    </v-flex>
                    <v-flex xs12 class="text-xs-center py-3">
                        <h1 class="font-weight-light">Manual and time- Consuming process to consider all the
                            commodities/ components to identify best suited configuration (Bill of Material) and its
                            rollup cost.</h1>
                    </v-flex>
                    <v-flex xs12 class="text-xs-center">
                         <h1 class="font-weight-regular">Benefits : – Business can finalize the product platform configuration based on different
                        criterion.
                        <br>
                        – Pro-active Supplier Engagement.
                        <br>
                        – Automated Process
                        <br>
                        – Reduce Time <br></h1>
                    </v-flex>
                </v-layout>
            </section>
            
            <v-footer height="auto">
                <v-layout row wrap>
                    <v-flex xs12>
                        <v-card flat tile class="primary lighten-1 white--text text-xs-center">
                            <v-card-text>
                                <v-btn v-for="icon in icons" :href="icon.link" :key="icon.social" class="mx-3 white--text" icon>
                                    <v-icon size="24px">{{ icon.social }}</v-icon>
                                </v-btn>
                            </v-card-text>
                            <v-card-text class="mb-2">
                                <h3 class="font-weight-light">
                                    We would love to hear what you think. Drop us a line, whether it is praise or criticism, a question, a suggestion or just a hello. Go ahead and send it!</h3>
                                <h2>Dell</h2>
                            </v-card-text>

                            <v-divider></v-divider>

                            <v-card-text class="white--text">
                                &copy;2019 — <strong>DELL Hack.2.Hire</strong>
                            </v-card-text>
                        </v-card>
                    </v-flex>
                </v-layout>
            </v-footer>

        </v-content>
    </v-app>
</section>
</template>

<script>
import axios from "axios";
import router from "../router/index";
import logo from '@/assets/logo.svg'
export default {
    data: function () {
        return {
            icons: [{
                    social: "fab fa-facebook",
                    link: "https://www.facebook.com/Dell/"
                },
                {
                    social: "fab fa-twitter",
                    link: "https://twitter.com/Dell"
                },
                {
                    social: "fab fa-google-plus",
                    link: "https://plus.google.com/117161668189080869053"
                },
                {
                    social: "fab fa-linkedin",
                    link: "https://www.linkedin.com/company/dell/?originalSubdomain=in"
                },
                {
                    social: "fab fa-instagram",
                    link: "https://www.instagram.com/dell/"
                }
            ],
            logo: logo,
            valid: false,
            name: "",
            contact: "",
            email: "",
            message: "",
            nameRules: [v => !!v || "Required"],
            contactRules: [
                v => !!v || "Contact number  is required",
                v => (v && v.length == 10) || "Must be of 10 characters"
            ],
            messageRules: [
                v => !!v || "Required",
                v => (v && v.length <= 250) || "Must be less than 250 characters"
            ],
            emailRules: [
                v => !!v || "E-mail is required",
                v => /.+@.+/.test(v) || "E-mail must be valid"
            ]
        };
    },
    computed: {
        userstatus() {
            if (
                this.$store.getters.getUserId !== null &&
                this.$store.getters.getUserId !== undefined
            ) {
                return "/dashboard";
            } else {
                return "/signin";
            }
        },
        error() {
            return this.$store.getters.error;
        },
        success() {
            return this.$store.getters.success;
        },
        loading() {
            return this.$store.getters.loading;
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
    },
    methods: {
        sendresp() {
            var name = this.name
            var email = this.email
            var message = this.message
            var contact = this.contact
            // console.log(name)       
            // console.log(email)       
            // console.log(message)       
            // console.log(contact)       
            var formData = new FormData();
            formData.append('email', email);
            formData.append('name', name);
            formData.append('message', message);
            formData.append('contact', contact);
            self = this;
            axios
                .post("https://www.mujquiz.com/contactus.php", formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data',
                        "Access-Control-Allow-Origin": "*"
                    }
                })
                .then(function (response) {
                    if (response.data.status == "true") {
                        self.$store.commit("setSuccess", {
                            message: "Your response has been collected. We will reply to you shortly",
                            status: true
                        });
                        console.log('Sent')
                    }
                    self.reset();
                })
                .catch(error => {
                    self.$store.commit("setError", {
                        message: "Server Not Responding. Try Again Later",
                        status: true
                    });
                    console.log('Error')
                    self.reset();
                });
        },
        reset() {
            this.$refs.form.reset();
        }
    }
};
</script>

<style lang="css" scoped>
@keyframes bounce {

    0%,
    20%,
    60%,
    100% {
        -webkit-transform: translateY(0);
        transform: translateY(0);
    }

    40% {
        -webkit-transform: translateY(-20px);
        transform: translateY(-20px);
    }

    80% {
        -webkit-transform: translateY(-10px);
        transform: translateY(-10px);
    }
}

a {
    color: black;
    text-decoration: none;
}

.image img {
    -webkit-transition: all 1s ease;
    /* Safari and Chrome */
    -moz-transition: all 1s ease;
    /* Firefox */
    -ms-transition: all 1s ease;
    /* IE 9 */
    -o-transition: all 1s ease;
    /* Opera */
    transition: all 1s ease;
}

.image:hover img {
    -webkit-transform: scale(1.25);
    /* Safari and Chrome */
    -moz-transform: scale(1.25);
    /* Firefox */
    -ms-transform: scale(1.25);
    /* IE 9 */
    -o-transform: scale(1.25);
    /* Opera */
    transform: scale(1.25);
}

/* button{
    position: relative;
    display: inline-block;
    font-weight: bold;   
    text-decoration: none;
    color: #00BCD4;
    background: #ECECEC; 
    transition: .4s;
}*/
button:hover {
    animation: bounce 1s;
    text-shadow: 0px 0px 0px rgba(255, 255, 255, 1);
    -webkit-box-shadow: 0px 5px 40px -10px rgba(0, 0, 0, 0.57);
    -moz-box-shadow: 0px 5px 40px -10px rgba(0, 0, 0, 0.57);
    transition: all 0.4s ease 0s;
    /* transform: skew(-29deg); */
}

.element {
    /* border-radius: 0 0 150% 150% / 20%; */
    /* clip-path: polygon(0 0,100% 0,100% 100%,0 100vh) */
    /* Note that percentages work as well as px */
}

.element2 {
    border-radius: 150% 150% 0 0/ 30%;

    /* clip-path: polygon(0 0,100% 0,100% 100%,0 100vh) */
    /* Note that percentages work as well as px */
}
</style>
