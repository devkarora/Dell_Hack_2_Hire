<template>
<v-layout row wrap>
    <v-flex xs12 class="text-xs-center">
        <h1 class="display-1 font-weight-regular">
            <v-icon class="mr-2" color="green" size="35">fas fa-dollar-sign</v-icon>
            Cost Prediction
        </h1>
        <span>Select the product to get the cost</span>
    </v-flex>
    <v-flex xs12>
        <v-container>
            <v-layout row wrap>
                <v-flex xs12 sm6 class="text-xs-center mt-2 px-2">
                    <router-link to="/laptopcost">
                        <v-card class="purple lighten-4" hover raised>
                            <v-avatar size="250">
                                <v-icon color="grey darken-3" size="150">fas fa-laptop</v-icon>
                            </v-avatar>
                            <v-card color="grey">
                                <h1 class="font-weight-light display-1">Laptop</h1>
                            </v-card>
                        </v-card>
                    </router-link>
                </v-flex>
                <v-flex xs12 sm6 class="text-xs-center mt-2 px-2">
                    <router-link to="/desktopcost">
                        <v-card color="teal lighten-4" raised hover class="">
                            <v-avatar size="250">
                                <v-icon size="190" color="grey darken-3">desktop_windows</v-icon>
                            </v-avatar>
                            <v-card color="grey">
                                <h1 class="font-weight-light display-1">Desktop</h1>
                            </v-card>
                        </v-card>
                    </router-link>
                </v-flex>
            </v-layout>
        </v-container>
    </v-flex>
</v-layout>
</template>

<script>
export default {
    data() {
        return {

        }
    }
}
</script>

<style scoped>
a {
    text-decoration: none;
}
</style>
