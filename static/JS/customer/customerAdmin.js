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
    

    const ctx1 = document.getElementById('myChart1');
  
    new Chart(ctx1, {
      type: 'bar',
      data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [
        {
          label: '# of people voted',
          data: [12, 19, 3, 5, 2, 3],
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
        },{
            label: '# of not voted',
            data: [1,9, 3, 5, 2, 3],
            borderWidth: 1,
            backgroundColor: [
          'rgba(255, 99, 132, 0.6)',
          'rgba(255, 159, 64, 0.6)',
          'rgba(255, 205, 86, 0.6)',
          'rgba(75, 192, 192, 0.6)',
          'rgba(54, 162, 235, 0.6)',
          'rgba(153, 102, 255, 0.6)',
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
          },
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

    const ctx2 = document.getElementById('myChart2');
  
    new Chart(ctx2, {
      type: 'line',
      data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [
        {
          label: '# of people voted',
          data: [12, 19, 3, 5, 2, 3],
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
        },{
            label: '# of not voted',
            data: [1,9, 3, 5, 2, 3],
            borderWidth: 1,
            backgroundColor: [
          'rgba(255, 99, 132, 0.6)',
          'rgba(255, 159, 64, 0.6)',
          'rgba(255, 205, 86, 0.6)',
          'rgba(75, 192, 192, 0.6)',
          'rgba(54, 162, 235, 0.6)',
          'rgba(153, 102, 255, 0.6)',
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
          },
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

    const donut = document.getElementById('donut');
  
    new Chart(donut, {
      type: 'doughnut',
      data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [ 
        {
          label: '# of people voted',
          data: [12, 19, 3, 5, 2, 3],
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
        },{
            label: '# of not voted',
            data: [1,9, 3, 5, 2, 3],
            borderWidth: 1,
            backgroundColor: [
          'rgba(255, 99, 132, 0.6)',
          'rgba(255, 159, 64, 0.6)',
          'rgba(255, 205, 86, 0.6)',
          'rgba(75, 192, 192, 0.6)',
          'rgba(54, 162, 235, 0.6)',
          'rgba(153, 102, 255, 0.6)',
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
          },
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


    const pie = document.getElementById('pie');
  
    new Chart(pie, {
      type: 'radar',
      data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [
        {
          label: '# of people voted',
          data: [12, 19, 3, 5, 2, 3],
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
        },{
            label: '# of not voted',
            data: [1,9, 3, 5, 2, 3],
            borderWidth: 1,
            backgroundColor: [
          'rgba(255, 99, 132, 0.6)',
          'rgba(255, 159, 64, 0.6)',
          'rgba(255, 205, 86, 0.6)',
          'rgba(75, 192, 192, 0.6)',
          'rgba(54, 162, 235, 0.6)',
          'rgba(153, 102, 255, 0.6)',
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
          },
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

    

    function moveToOverview(){
       document.getElementById('overView').style.backgroundColor = 'rgba(226, 226, 226, 0.411)';
       document.getElementById('middle').style.transform = 'translateY(0px)';
       document.getElementById('thirdDiv').style.transform = 'translateY(0px)';
       document.getElementById('customer').style.backgroundColor = 'white';
       document.getElementById('addItems').style.backgroundColor = 'white';
       document.getElementById('graphView').style.backgroundColor = 'white';
    }

    function movetoCustomer(){
     document.getElementById('middle').style.transform = 'translateY(-900px)';
     document.getElementById('thirdDiv').style.transform = 'translateY(-900px)';
     document.getElementById('customer').style.backgroundColor = 'rgba(226, 226, 226, 0.411)';
     document.getElementById('overView').style.backgroundColor = 'white';
     document.getElementById('addItems').style.backgroundColor = 'white';
     document.getElementById('graphView').style.backgroundColor = 'white';
  }

    function movetoAdditems(){
       document.getElementById('addItems').style.backgroundColor = 'rgba(226, 226, 226, 0.411)';
       document.getElementById('middle').style.transform = 'translateY(-1800px)';
       document.getElementById('thirdDiv').style.transform = 'translateY(-1800px)';
       document.getElementById('customer').style.backgroundColor = 'white';
       document.getElementById('overView').style.backgroundColor = 'white';
       document.getElementById('graphView').style.backgroundColor = 'white';
    }

    function movetoGraph(){
       document.getElementById('addItems').style.backgroundColor = 'white';
       document.getElementById('graphView').style.backgroundColor = 'rgba(226, 226, 226, 0.411)';
       document.getElementById('middle').style.transform = 'translateY(-2700px)';
       document.getElementById('thirdDiv').style.transform = 'translateY(-2700px)';
       document.getElementById('customer').style.backgroundColor = 'white';
       document.getElementById('overView').style.backgroundColor = 'white';
    }





    function displayImage(event) {
     var fileInput = event.target;
     var imageDisplay = document.getElementById('imageDisplay');
 
     if (fileInput.files && fileInput.files[0]) {
       var reader = new FileReader();
 
       reader.onload = function(e) {
         imageDisplay.src = e.target.result;
         document.getElementById('imageDisplay').style.boxShadow='0 4px 8px 0 rgba(0, 0, 0, 0.06), 0 6px 20px 0 rgba(0, 0, 0, 0.071)'
       };
 
       reader.readAsDataURL(fileInput.files[0]);
     }
   }