import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomepageComponent } from './pages/homepage/homepage.component';
import { TanksdetailComponent } from './pages/tanksdetail/tanksdetail.component';
import { OutputsComponent } from './pages/outputs/outputs.component';
import { InputscreenComponent } from './pages/inputscreen/inputscreen.component';

const routes: Routes = [
	{ path: '', component: HomepageComponent },
	{ path: 'tanksdetails', component: TanksdetailComponent },
	{ path: 'inputs', component: InputscreenComponent },
	{ path: 'outputs', component: OutputsComponent }
];

@NgModule({
	imports: [ RouterModule.forRoot(routes) ],
	exports: [ RouterModule ]
})
export class AppRoutingModule {}
