<template>
<v-app>
    <v-navigation-drawer v-model="drawer" :mini-variant.sync="mini" fixed clipped app width="240">
        <v-img :aspect-ratio="16/9" :src="drawerimg">
            <v-layout pa-2 column fill-height class="lightbox white--text">
                <v-spacer></v-spacer>
                <v-flex shrink v-if="!mini">
                    <div class="subheading">{{ name }}</div>
                    <div class="body-1">{{ email }}</div>
                </v-flex>
            </v-layout>
        </v-img>
        <v-progress-linear v-if="loading" class="mt-0" height="2" color="accent" :indeterminate="loading"></v-progress-linear>
        <div></div>

        <v-list>
            <template v-if="!userIsAuthenticated" v-for="(item, i) in menuItems">
                <v-divider v-if="item.divider" :key="i"></v-divider>
                <v-list-tile v-else :key="item.title" :to="item.link">
                    <v-list-tile-action>
                        <v-icon>{{ item.icon }}</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-title color="primary">{{ item.text }}</v-list-tile-title>
                </v-list-tile>
            </template>
            <template>
                <v-list-tile v-if="userIsAuthenticated" to="/dashboard">
                    <v-list-tile-action>
                        <v-icon>dashboard</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-title color="primary">Dashboard</v-list-tile-title>
                </v-list-tile>
            </template>
            <template>
                <v-list-tile v-if="userIsAuthenticated" to="/costpred">
                    <v-list-tile-action>
                        <v-icon>fas fa-money-check-alt</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-title color="primary">Cost Prediction</v-list-tile-title>
                </v-list-tile>
            </template>
            <template>
                <v-list-tile v-if="userIsAuthenticated" to="/getconfig">
                    <v-list-tile-action>
                        <v-icon>fas fa-clipboard-check</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-title color="primary">Get Configuration</v-list-tile-title>
                </v-list-tile>
            </template>
                <template>
                <v-list-tile v-if="userIsAuthenticated" to="/orders">
                    <v-list-tile-action>
                        <v-icon>fas fa-folder</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-title color="primary">Order Summary</v-list-tile-title>
                </v-list-tile>
            </template>         
            <v-divider v-if="userIsAuthenticated"></v-divider>
            <template>
                <v-list-tile v-if="userIsAuthenticated" @click="onLogout">
                    <v-list-tile-action>
                        <v-icon color="error">power_settings_new</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-title color="primary">Logout</v-list-tile-title>
                </v-list-tile>
            </template>
        </v-list>
    </v-navigation-drawer>
    <v-toolbar flat class="primary" app clipped-left fixed>
        <v-toolbar-side-icon v-if="!mini" @click.native="drawer = !drawer" class="white--text"></v-toolbar-side-icon>
        <router-link to="/">
            <img height="23" :src="logo" alt="logo">
        </router-link>
        <v-spacer></v-spacer>

        <v-btn flat v-if="userIsAuthenticated" @click="onLogout">
            <v-icon class="white--text mr-2">fas fa-sign-out-alt</v-icon>
            <span class="white--text mr-1">LOGOUT</span>
        </v-btn>
    </v-toolbar>
    <v-content>
        <v-container fluid fill-height>
            <router-view></router-view>
        </v-container>
    </v-content>
</v-app>
</template>

<script>
import drawerimg from "@/assets/profile_background.jpg";
import logo from "@/assets/logo2.png"
export default {
    data: () => ({
        logo: logo,
        drawer: null,
        drawerimg: drawerimg,
        mini: false
    }),
    computed: {
        menuItems() {
            let menuItems = [{
                icon: "person",
                text: "Sign In",
                link: "/signin"
            }];
            return menuItems;
        },
        userIsAuthenticated() {
            return (
                this.$store.getters.getUserId !== null &&
                this.$store.getters.getUserId !== undefined
            );
        },
        name() {
            if (this.userIsAuthenticated)
                return "Lokesh Dugar";
            else
                return ""
        },
        email() {
            if (this.userIsAuthenticated)
                return "lokeshdugarld@gmail.com";
            else
                return ""
        },
        contact() {
            if (this.userIsAuthenticated)
                return "9830588848";
            else
                return ""
        },
        loading() {
            return this.$store.getters.loading;
        }
    },
    methods: {
        onLogout() {
            this.$store.dispatch("logout");
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
};
</script>
