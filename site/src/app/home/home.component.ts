import {Component} from "@angular/core";
// import {NetworkingService} from "../networking/networking.service";

@Component({
    selector: 'home',
    template: require('./home.component.html'),
    // providers:[NetworkingService]
})

export class HomeComponent {
    // ns: NetworkingService;
    foo: String = "Hello";

    // constructor(ns:NetworkingService) {
    //     this.ns = ns;
    // }

}
