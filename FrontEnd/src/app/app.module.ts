import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {HttpClientModule} from '@angular/common/http';
import { NavigationbarComponent } from './components/navigationbar/navigationbar.component';
import { AlltanksComponent } from './components/alltanks/alltanks.component';
import { InputparametersComponent } from './components/inputparameters/inputparameters.component';
import { OutputparametersComponent } from './components/outputparameters/outputparameters.component';
import { MonthlyplanningComponent } from './components/navigationbar/monthlyplanning/monthlyplanning.component';
import { NewnaphthaComponent } from './components/navigationbar/newnaphtha/newnaphtha.component';
import { HomeComponent } from './components/navigationbar/home/home.component';
import { InputoutputComponent } from './components/navigationbar/inputoutput/inputoutput.component';
import { LoginComponent } from './components/navigationbar/login/login.component';
import { Tankno1Component } from './components/alltanks/tankno1/tankno1.component';
import { Tankno2Component } from './components/alltanks/tankno2/tankno2.component';
import { Tankno3Component } from './components/alltanks/tankno3/tankno3.component';
import { Tankno4Component } from './components/alltanks/tankno4/tankno4.component';
import { Tankno5Component } from './components/alltanks/tankno5/tankno5.component';
import { UserdefinedinputsComponent } from './components/inputparameters/userdefinedinputs/userdefinedinputs.component';
import { ModelinputscomparionComponent } from './components/inputparameters/modelinputscomparion/modelinputscomparion.component';
import { InputsComponent } from './components/inputparameters/userdefinedinputs/inputs/inputs.component';
import { BlendqualityComponent } from './components/inputparameters/userdefinedinputs/blendquality/blendquality.component';
import { RunninginputComponent } from './components/inputparameters/modelinputscomparion/runninginput/runninginput.component';
import { ProfitmaxinputComponent } from './components/inputparameters/modelinputscomparion/profitmaxinput/profitmaxinput.component';
import { BestfitinputComponent } from './components/inputparameters/modelinputscomparion/bestfitinput/bestfitinput.component';
import { NexthourinputComponent } from './components/inputparameters/modelinputscomparion/nexthourinput/nexthourinput.component';
import { UserdefinedinputsummaryComponent } from './components/outputparameters/userdefinedinputsummary/userdefinedinputsummary.component';
import { RunninginputsummaryComponent } from './components/outputparameters/runninginputsummary/runninginputsummary.component';
import { ProfitmaxinputsummaryComponent } from './components/outputparameters/profitmaxinputsummary/profitmaxinputsummary.component';
import { BestfitinputsummaryComponent } from './components/outputparameters/bestfitinputsummary/bestfitinputsummary.component';
import { NexthourinputsummaryComponent } from './components/outputparameters/nexthourinputsummary/nexthourinputsummary.component';
import { UserdefinedoutputComponent } from './components/outputparameters/userdefinedoutput/userdefinedoutput.component';
import { RunningoutputComponent } from './components/outputparameters/runningoutput/runningoutput.component';
import { ProfitmaxoutputComponent } from './components/outputparameters/profitmaxoutput/profitmaxoutput.component';
import { BestfitoutputComponent } from './components/outputparameters/bestfitoutput/bestfitoutput.component';
import { NexthouroutputComponent } from './components/outputparameters/nexthouroutput/nexthouroutput.component';
import { QualityquantityComponent } from './components/navigationbar/qualityquantity/qualityquantity.component';
import { ModelblendqualityComponent } from './components/inputparameters/modelblendquality/modelblendquality.component';
import { BlendcomparisonComponent } from './components/inputparameters/blendcomparison/blendcomparison.component';
import { RunningqualityComponent } from './components/inputparameters/modelblendquality/runningquality/runningquality.component';
import { ProfitmaxqualityComponent } from './components/inputparameters/modelblendquality/profitmaxquality/profitmaxquality.component';
import { BestfitqualityComponent } from './components/inputparameters/modelblendquality/bestfitquality/bestfitquality.component';
import { NexthourqualityComponent } from './components/inputparameters/modelblendquality/nexthourquality/nexthourquality.component';
import { NirblendqualityComponent } from './components/inputparameters/blendcomparison/nirblendquality/nirblendquality.component';
import { ModelnirblendqualityComponent } from './components/inputparameters/blendcomparison/modelnirblendquality/modelnirblendquality.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';





@NgModule({
  declarations: [
    AppComponent,
    NavigationbarComponent,
    AlltanksComponent,
    InputparametersComponent,
    OutputparametersComponent,
    MonthlyplanningComponent,
    NewnaphthaComponent,
    HomeComponent,
    InputoutputComponent,
    LoginComponent,
    Tankno1Component,
    Tankno2Component,
    Tankno3Component,
    Tankno4Component,
    Tankno5Component,
    UserdefinedinputsComponent,
    ModelinputscomparionComponent,
    InputsComponent,
    BlendqualityComponent,
    RunninginputComponent,
    ProfitmaxinputComponent,
    BestfitinputComponent,
    NexthourinputComponent,
    RunninginputsummaryComponent,
    ProfitmaxinputsummaryComponent,
    BestfitinputsummaryComponent,
    NexthourinputsummaryComponent,
    UserdefinedoutputComponent,
    RunningoutputComponent,
    ProfitmaxoutputComponent,
    BestfitoutputComponent,
    NexthouroutputComponent,
    QualityquantityComponent,
    ModelblendqualityComponent,
    BlendcomparisonComponent,
    RunningqualityComponent,
    ProfitmaxqualityComponent,
    BestfitqualityComponent,
    NexthourqualityComponent,
    NirblendqualityComponent,
    ModelnirblendqualityComponent,
    UserdefinedinputsummaryComponent,
    
    
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    AppRoutingModule,
    NgbModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
