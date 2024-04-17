const ctx = document.getElementById('myChart');
    fetch('/totalViews').then(res => res.json()).then(
      data => {
      new Chart(ctx, {
        type: 'line',
        data: {
          labels:data.lable,
          datasets: [
          {
            label: 'Customer Growth ',
            data:data.data,
            borderWidth: 1,
            backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
          'rgba(255, 159, 64, 0.2)',
          'rgba(255, 205, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(153, 102, 255, 0.2)',
          'rgba(201, 203, 207, 0.2)'
        ],borderColor: [
        'rgb(255, 99, 132)',
        'rgb(255, 159, 64)',
        'rgb(255, 205, 86)',
        'rgb(75, 192, 192)',
        'rgb(54, 162, 235)',
        'rgb(153, 102, 255)',
        'rgb(201, 203, 207)'
              ],
          }
          ]
        },
        
        options: {
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });
    });
    
    function movetoCustomer(){
      document.getElementById('middle').style.transform = 'translateY(-700px)';
      document.getElementById('thirdDiv').style.transform = 'translateY(-700px)';
      document.getElementById('customer').style.backgroundColor = 'rgba(226, 226, 226, 0.411)';
      document.getElementById('overView').style.backgroundColor = 'white';
      document.getElementById('addItems').style.backgroundColor = 'white';
   }

   function moveToOverview(){
      document.getElementById('overView').style.backgroundColor = 'rgba(226, 226, 226, 0.411)';
      document.getElementById('middle').style.transform = 'translateY(0px)';
      document.getElementById('thirdDiv').style.transform = 'translateY(0px)';
      document.getElementById('customer').style.backgroundColor = 'white';
      document.getElementById('addItems').style.backgroundColor = 'white';
   }

   function movetoAdditems(){
      document.getElementById('addItems').style.backgroundColor = 'rgba(226, 226, 226, 0.411)';
      document.getElementById('middle').style.transform = 'translateY(-1400px)';
      document.getElementById('thirdDiv').style.transform = 'translateY(0px)';
      document.getElementById('customer').style.backgroundColor = 'white';
      document.getElementById('overView').style.backgroundColor = 'white';
   }