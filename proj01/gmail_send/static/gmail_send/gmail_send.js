// -----------------------------------------------------------------------
//	gmail_send.js
//
//					Dec/30/2018
//
// -----------------------------------------------------------------------
jQuery (function ()
{
	jQuery("#outarea_aa").html ("*** gmail_send.js *** start *** Dec/30/2018 ***")

	click_check_proc ()

	jQuery("#outarea_hh").html ("*** gmail_send.js *** end *** Dec/30/2018 ***")
})

// -----------------------------------------------------------------------
function click_check_proc ()
{
	jQuery ("button.check").click (function ()
		{
		var str_out = "*** clicked ***<br />"
		jQuery("#outarea_bb").html(str_out)

		const url = "/gmail_send/main/"

		var params = {}
		params['mail_to'] = jQuery("#mail_to").val()
		params['subject'] = jQuery("#subject").val()

		params['str_message'] = jQuery("#str_text").val()

		var str_out = ""
		str_out += params['mail_to'] + "<br />"
		str_out += params['subject'] + "<br />"
		str_out += params['str_message'] + "<br />"

		jQuery("#outarea_cc").html(str_out)

		jQuery.post(url,params,function ()
			{
			var str_tmp = "*** check *** ccc ***<br />"
			jQuery("#outarea_ee").html(str_tmp)
			})
		})
}

// -----------------------------------------------------------------------
