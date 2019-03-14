<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>

    <!-- Jumbotron -->
    <div class="jumbotron text-center" style="margin-bottom:0">
  <h1>{{'project_name'}} {{'part_description'}} {{'part_no'}}</h1>
  <p>Addtional Request here...</p>
</div>

    <!-- Navbar -->
<nav class="navbar navbar-expand-sm bg-dark navbar-dark">
  <a class="navbar-brand" href="#">Navbar</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="collapsibleNavbar">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="#">Link</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Link</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Link</a>
      </li>
    </ul>
  </div>
</nav>

    <!-- Content -->
<div class="container" style="margin-top:30px">
  <form action="/quotation" method="POST">
    <!-- Piece Price CBD -->

    <div class="form-row">
    <h1>Cost Break Down</h1>
        <legend>Material</legend>

        <div class="form-group col-md-2">
      <label for="part_weight">Part Weight</label>
      <input type="text" class="form-control" name="part_weight">
        </div>

        <div class="form-group col-md-2">
      <label for="runner_weight">Runner Weight/part</label>
      <input type="text" class="form-control" name="runner_weight">
        </div>

        <div class="form-group col-md-2">
      <label for="wastage">Wastage</label>
      <input type="text" class="form-control" name="wastage">
        </div>

        <div class="form-group col-md-2">
      <label for="resin_moq">Resin MOQ</label>
      <input type="text" class="form-control" name="resin_moq">
        </div>

        <div class="form-group col-md-2">
      <label for="resin_price">Resin Price</label>
      <input type="text" class="form-control" name="resin_price">
        </div>

    </div>

    <div class="form-row">
        <legend>Injection Process</legend>

        <div class="form-group col-md-2">
      <label for="cavity">Cavity</label>
      <input type="text" class="form-control" name="cavity">
        </div>

        <div class="form-group col-md-2">
      <label for="machine_tonnage">Machine Tonnage</label>
      <input type="text" class="form-control" name="machine_tonnage">
        </div>

        <div class="form-group col-md-2">
      <label for="machine_rate">Machine Rate/Hour</label>
      <input type="text" class="form-control" name="machine_rate">
        </div>

        <div class="form-group col-md-2">
      <label for="cycle_time">Cycle Time</label>
      <input type="text" class="form-control" name="cycle_time">
        </div>

        <div class="form-group col-md-2">
      <label for="reject_allow">Reject allow</label>
      <input type="text" class="form-control" name="reject_allow">
        </div>
    </div>

    <div class="form-row">
        <legend>Second Process</legend>

        <div class="form-group col-md-2">
          <label for="2ndp_mtl">Material Name</label>
      <input type="text" class="form-control" name="2ndp_mtl">
        </div>

        <div class="form-group col-md-2">
      <label for="2ndp_mtl_cost">Material Cost</label>
      <input type="text" class="form-control" name="2ndp_mtl_cost">
        </div>

        <div class="form-group col-md-2">
      <label for="2ndp_process">Process Name</label>
      <input type="text" class="form-control" name="2ndp_procss">
        </div>

        <div class="form-group col-md-2">
      <label for="2ndp_process_cost">Process Cost</label>
      <input type="text" class="form-control" name="2ndp_process_cost">
        </div>

    </div>


    <div class="form-row">
        <legend>Trans & Packs</legend>

        <div class="form-group col-md-2">
      <label for="part_moq">Part MOQ</label>
      <input type="text" class="form-control" name="part_moq">
        </div>

        <div class="form-group col-md-2">
      <label for="packaging_concept">Packaging Concept</label>
      <input type="text" class="form-control" name="packaging_concept">
        </div>

        <div class="form-group col-md-2">
      <label for="packaging_cost">Packaging Cost</label>
      <input type="text" class="form-control" name="packaging_cost">
        </div>

        <div class="form-group col-md-2">
      <label for="cycle_time">Transportation Cost</label>
      <input type="text" class="form-control" name="cycle_time">
        </div>

    </div>

    <div class="form-row">
        <legend>SG&A</legend>

        <div class="form-group col-md-2">
      <label for="profit">Profit</label>
      <input type="text" class="form-control" name="profit">
        </div>

        <div class="form-group col-md-2">
      <label for="overhead">Overhead</label>
      <input type="text" class="form-control" name="overhead">
        </div>
    </div>

    <hr>

    <!-- Investment -->

 <div class="form-row">
    <h1>Investment</h1>
        <legend>Injection Tooling</legend>
        <div class="form-group col-md-2">
      <label for="tooling_lifetime">Tooling Lifetime</label>
      <input type="text" class="form-control" name="tooling_lifetime">
        </div>

        <div class="form-group col-md-2">
      <label for="tooling_cost">Tooling Cost</label>
      <input type="text" class="form-control" name="tooling_cost">
        </div>

        <div class="form-group col-md-2">
      <label for="measuring_cost">Measuring Cost</label>
      <input type="text" class="form-control" name="measuring_cost">
        </div>

        <div class="form-group col-md-2">
      <label for="copy_tooling_cost">Copy Tooling Cost</label>
      <input type="text" class="form-control" name="copy_tooling_cost">
        </div>

    </div>

 <div class="form-row">
        <legend>Additional</legend>
        <div class="form-group col-md-2">
      <label for="tooling_lifetime">Extra Tooling Name</label>
      <input type="text" class="form-control" name="tooling_lifetime">
        </div>

        <div class="form-group col-md-2">
      <label for="tooling_cost">Extra Tooling Cost</label>
      <input type="text" class="form-control" name="tooling_cost">
        </div>

        <div class="form-group col-md-2">
      <label for="copy_tooling_cost">Extra Investment Name</label>
      <input type="text" class="form-control" name="copy_tooling_cost">
        </div>

        <div class="form-group col-md-2">
      <label for="copy_tooling_cost">Extra Investment Cost</label>
      <input type="text" class="form-control" name="copy_tooling_cost">
        </div>
    </div>

        <hr>

 <div class="form-row">
    <h1>Price Detail</h1>
        <legend>Yearly Price in 100pcs</legend>
        <div class="form-group col-md-1">
      <label for="year1_price">Year-1 Price</label>
      <input type="text" class="form-control" name="year1_price">
        </div>

        <div class="form-group col-md-1">
      <label for="year2_price">Year-2 Price</label>
      <input type="text" class="form-control" name="year2_price">
        </div>

        <div class="form-group col-md-1">
      <label for="year3_price">Year-3 Price</label>
      <input type="text" class="form-control" name="year3_price">
        </div>

        <div class="form-group col-md-1">
      <label for="year4_price">Year-4 Price</label>
      <input type="text" class="form-control" name="year4_price">
        </div>

        <div class="form-group col-md-1">
      <label for="year5_price">Year-5 Price</label>
      <input type="text" class="form-control" name="year5_price">
        </div>

        <div class="form-group col-md-1">
      <label for="year6_price">Year-6 Price</label>
      <input type="text" class="form-control" name="year6_price">
        </div>

        <div class="form-group col-md-1">
      <label for="year7_price">Year-7 Price</label>
      <input type="text" class="form-control" name="year7_price">
        </div>

        <div class="form-group col-md-1">
      <label for="year8_price">Year-8 Price</label>
      <input type="text" class="form-control" name="year9_price">
        </div>

        <div class="form-group col-md-1">
      <label for="year10_price">Year-10 Price</label>
      <input type="text" class="form-control" name="year10_price">
        </div>
 </div>


 <div class="form-row">
        <legend>Quick Saving</legend>
        <div class="form-group col-md-2">
      <label for="1st_qc_amount">1st 50% QS Amount</label>
      <input type="text" class="form-control" name="1st_qc_amount">
        </div>

        <div class="form-group col-md-2">
      <label for="1st_qc_date">1st 50% QS Date</label>
      <input type="text" class="form-control" name="1st_qc_date">
        </div>

        <div class="form-group col-md-2">
      <label for="2nd_qc_amount">2nd 50% QS Amount</label>
      <input type="text" class="form-control" name="2nd_qc_amount">
        </div>

        <div class="form-group col-md-2">
      <label for="2nd_qc_date">2nd 50% QS Date</label>
      <input type="text" class="form-control" name="2nd_qc_date">
        </div>

 </div>

 <hr>

 <input class="btn btn-primary btn-lg btn-block" type="submit" name="save" value="Confirm The Price">

<br>

  </form>
  </div>
</div>



<div class="jumbotron text-center" style="margin-bottom:0">
  <p>Footer</p>
</div>


    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </body>
</html>
