<template>
<v-layout row wrap>
    <v-flex xs12>
        <v-layout row wrap>
            <v-flex xs12 class="text-xs-center">
                <h1 class="display-1 font-weight-regular">
                    <v-icon class="mr-2" color="brown" size="35">fas fa-cart-plus</v-icon>Order Summary
                </h1>
            </v-flex>
            <v-flex xs12 class="py-5">
                <v-data-table :headers="headers" :items="itemss" class="elevation-1"  item-key="name">

                    <template slot="items" slot-scope="props">
                        <td class="text-xs-center">{{ props.item.order.processor }}</td>
                        <td class="text-xs-center">{{ props.item.order.ram }}</td>
                        <td class="text-xs-center">{{ props.item.order.gc }}</td>
                        <td class="text-xs-center">{{ props.item.order.mouse }}</td>
                        <td class="text-xs-center">{{ props.item.order.keyboard }}</td>
                        <td class="text-xs-center">{{ props.item.order.hdd }}</td>
                        <td class="text-xs-center">{{ props.item.order.screen }}</td>
                        <td class="text-xs-center">{{ props.item.order.cost }}</td>
                    </template>
                    <template slot="no-data">
                        <div class="text-xs-center">No Order</div>
                    </template>
                </v-data-table>
            </v-flex>
        </v-layout>
    </v-flex>
</v-layout>
</template>

<script>
export default {
    data() {
        return {
            headers: [{
                    text: 'Processor',
                    align: 'left',
                    sortable: false,
                    value: 'name',
                },
                {
                    text: 'RAM',
                    value: 'calories'
                },
                {
                    text: 'GC',
                    value: 'fat'
                },
                {
                    text: 'Mouse',
                    value: 'carbs'
                },
                {
                    text: 'Keyboard',
                    value: 'protein'
                },
                {
                    text: 'HDD',
                    value: 'iron'
                },
                {
                    text: 'Screen',
                    value: 'iron'
                },
                {
                    text: 'Cost in $',
                    value: 'iron'
                },
            ],            
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
        itemss(){
            return this.$store.getters.getOrder
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
