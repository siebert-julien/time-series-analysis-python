$(document).ready(function() {
    $('#packages').DataTable( {
        scrollY:        true,
        scrollX:        true,
        scrollCollapse: true,
        paging:         false,
        fixedColumns:{leftColumns: 1},
        ajax: 'data/time-series-packages.json',
        sAjaxDataProp: "",
        columns: [
            {data: "url", "name": "name",
                fnCreatedCell: function (nTd, sData, oData, iRow, iCol) {
                    if(oData.name) {
                        $(nTd).html("<a href='"+oData.url+"'>"+oData.name+"</a>");
                    }
                }
            },
            {data:"forecasting"},
            {data:"clustering"},
            {data:"classification"},
            {data:"anomaly detection"},
            {data:"segmentation"},
            {data:"pattern recognition"},
            {data:"change point detection"},
            {data:"dimensionality reduction"},
            {data:"missing values imputation"},
            {data:"decomposition"},
            {data:"preprocessing"},
            {data:"similarity measures"},
            {data:"selection model hyperparameters features"},
            {data:"visualization"},
            {data:"metrics statistical tests"},
            {data:"synthetic data generation"},
            {data:"contains datasets"},
            {data:"dedicated documentation"},
            {data:"notebooks"},
            {data:"API reference"},
            {data:"install guide"},
            {data:"user guides"}
        ],
        initComplete: function () {
            var i = 0;
            this.api().columns().every( function () {
                var column = this;
                if(i>0){
                    var select = $('<select><option value=""></option></select>')
                        .appendTo( $(column.header()).empty() )
                        .on( 'change', function () {
                            var val = $.fn.dataTable.util.escapeRegex(
                                $(this).val()
                            );

                            column
                                .search( val ? '^'+val+'$' : '', true, false )
                                .draw();
                        } );

                    column.data().unique().sort().each( function ( d, j ) {
                        select.append( '<option value="'+d+'">'+d+'</option>' )
                    } );
                }
                i = i + 1;
            } );
        },
    } );
} );
