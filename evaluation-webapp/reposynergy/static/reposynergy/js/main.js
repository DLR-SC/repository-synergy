
$(document).ready( function() {
    render_readme_files()
    validate_synergy_direction($('input[type=radio][name=synergyQuestion]:checked').val())

   $('input[type=radio][name=synergyQuestion]').change(function() {
        validate_synergy_direction(this.value)

    });

   $('#annotated-form').submit(function(e) {
        $(".error").remove();
        var is_explanation_valid= validate_explanation()
        if(!is_explanation_valid) {
            e.preventDefault();
           $('#explanationtextarea').before('<div class="error alert-danger">Please enter an explanation for your answer (at least 50 characters) </div>');
           return false;
        } else {
            return true;
        }
    });


});


function render_readme_files() {
       var converter = new showdown.Converter({tables: true});

       var readme1= $('#hidden_readme1').val();
       var readme2= $('#hidden_readme2').val();

       $('#readme1').html( converter.makeHtml(readme1));
       $('#readme2').html( converter.makeHtml(readme2));
   }

function validate_synergy_direction(value){
    if (value === '1') {
        // disable direction radios and select None
        $('#directionQuestion-none').prop("checked", true);
        $('input[type=radio][name=directionQuestion]').attr('disabled', true);
    }
    else  if ( value !== 'undefined'){
        $('input[type=radio][name=directionQuestion]').attr('disabled', false);

        $('#directionQuestion-none').prop("checked", false);
        $('#directionQuestion-none').attr('disabled', true);

    }
}

function validate_explanation() {
      synergy =$('input[type=radio][name=synergyQuestion]:checked').val();
      if (synergy !== '1' &&   !$.trim($("#explanationtextarea").val()) ) {
           return false
      }
       return true
   }
